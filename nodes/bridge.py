"""
FF Bridge - наш священный мост между сырым выхлопом NodeToPython (grass.py,
clover.py, chamomile.py и др.) и остальной логикой аддона.

Таргет: Blender 5.2+. И слава богу, потому что начиная с 5.2 мы наконец-то 
можем вешать модификатор Geometry Nodes прямо на Empty! Никаких больше 
фейковых мешей-заглушек в проекте. Чистая оптимизация! ╰(*°▽°*)╯
"""

import bpy
import typing


# ============================================================================
#  Кэширование node group
# ============================================================================

def get_or_create_node_group(generator_func: typing.Callable, group_name: str):
    """
    Если мы не будем кэшировать нодовые группы, каждый клик по кнопке "Create"
    начнет плодить мутантские дубликаты (FF Grass Nodes.001, .002...). 
    Это жрет ресурсы и превращает .blend файл в помойку.
    
    Поэтому сначала ищем уже готовую группу, а если её нет - только тогда 
    дёргаем N2P-генератор и собираем граф.
    """
    existing = bpy.data.node_groups.get(group_name)
    if existing is not None:
        return existing

    node_tree_names: dict[typing.Callable, str] = {}
    node_group = generator_func(node_tree_names)
    node_group.is_modifier = True
    return node_group


# ============================================================================
#  Материалы, управляемые атрибутом ColorMask
# ============================================================================

def _srgb_to_linear(c: float) -> float:
    # Обычная математика конвертации, чтобы цвета в Blender не выглядели как кислота
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _hex_to_linear_rgba(hex_color: str):
    hex_color = hex_color.lstrip('#')
    r, g, b = (int(hex_color[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
    return (_srgb_to_linear(r), _srgb_to_linear(g), _srgb_to_linear(b), 1.0)


def get_or_create_colormask_material(mat_name: str, hex_color: str, attribute_name: str = "ColorMask"):
    """
    N2P по дефолту выплевывает абсолютно тупой материал, 
    который намертво красит Base Color и в упор не видит наш атрибут ColorMask. 
    Из-за этого крутилки цвета в UI идут лесом.
    
    Эта функция создает правильный, умный материал, который читает цвет из 
    геометрического графа через сокет "Grass/Clover/... Color". Бам! И полная 
    кастомизация цвета снова работает.
    """
    if mat_name in bpy.data.materials:
        return bpy.data.materials[mat_name]

    mat = bpy.data.materials.new(name=mat_name)
    mat.use_nodes = True
    nt = mat.node_tree
    bsdf = nt.nodes.get("Principled BSDF")
    
    if bsdf:
        bsdf.inputs["Base Color"].default_value = _hex_to_linear_rgba(hex_color)
        col_attr = nt.nodes.new("ShaderNodeAttribute")
        col_attr.attribute_name = attribute_name
        col_attr.location = (bsdf.location.x - 300, bsdf.location.y - 150)
        nt.links.new(col_attr.outputs["Color"], bsdf.inputs["Base Color"])
    return mat


def cleanup_unused_material(mat_name: str):
    """
    Метла для мусора. Некоторые старые версии N2P любят спавнить материалы 
    прямо в корне при каждом импорте модуля. Чтобы у нас не копились 
    ".001", ".002" при каждом перезапуске аддона, мы вызываем эту функцию 
    сразу после дампа. 
    
    Если материал оказался никому не нужен (0 юзеров) - безжалостно пускаем его под нож! 
    """
    mat = bpy.data.materials.get(mat_name)
    if mat is not None and mat.users == 0:
        bpy.data.materials.remove(mat)


# ============================================================================
#  Per-instance значения инпутов модификатора (Blender 5.2+ API)
# ============================================================================

def set_modifier_input(modifier, node_group, socket_name: str, value) -> bool:
    """
    ВНИМАНИЕ! Напоминалка для будущего меня: в Blender 5.2+ поменяли API.
    
    Раньше мы писали modifier["id"] = v. Теперь в 5.2 этот старый метод 
    НЕ кидает ошибку, он просто тупо молчит и ничего не делает! Искать этот 
    баг - чистая боль. Теперь пишем значения точечно через properties.inputs.

    И ради бога, НЕ ИСПОЛЬЗУЙ item.default_value как запасной план! 
    Это дефолт самой node group, он расшарен между ВСЕМИ объектами. 
    Поменяешь его тут - перекрасишь/сдвинешь вообще все деревья на сцене разом.
    """
    if not hasattr(node_group, "interface"):
        return False

    identifier = None
    for item in node_group.interface.items_tree:
        if (item.item_type == 'SOCKET'
                and getattr(item, 'in_out', 'INPUT') == 'INPUT'
                and item.name == socket_name):
            identifier = item.identifier
            break

    if identifier is None:
        return False

    socket = getattr(modifier.properties.inputs, identifier, None)
    if socket is None or not hasattr(socket, "value"):
        return False

    socket.value = value
    force_geonodes_refresh(modifier)
    return True


def force_geonodes_refresh(modifier):
    """
    Классический прикол Blender. Изменение инпута через Python не помечает граф 
    как "грязный". Вьюпорт тупо фризится и показывает старый результат, пока 
    юзер сам не потрогает крутилку в интерфейсе (трекеры #87006/#154890).
    
    Официального фикса пока нет, поэтому применяем дедовский костыль:
    выключили глазик, включили глазик (show_viewport). Форсируем пересчет! (⌐■_■)
    """
    modifier.show_viewport = False
    modifier.show_viewport = True


# ============================================================================
#  Спавн объекта с модификатором Geometry Nodes
# ============================================================================

def apply_geonodes_modifier(obj, node_group, mod_name: str = "GeometryNodes"):
    """
    Вешаем геоноды на объект.
    Если модификатор уже есть - просто скармливаем ему новую нод группу, 
    а не плодим дубликаты. Меньше дубликатов - легче сцене.
    """
    mod = obj.modifiers.get(mod_name)
    if mod is None:
        mod = obj.modifiers.new(name=mod_name, type='NODES')
    mod.node_group = node_group
    return mod


def spawn_object_with_geonodes(node_group, name: str = "FF_Object",
                                location=(0.0, 0.0, 0.0), link_to_scene: bool = True):
    """
    Спавним основу для генераторов "полного цикла" (grass/clover и т.д.).
    Тут мы строим геометрию с нуля. Начиная с Blender 5.2 мы можем вешать 
    модификатор прямо на Empty (object.data = None). Никаких orphan-мешей.
    """
    obj = bpy.data.objects.new(name, None)
    obj.location = location

    if link_to_scene:
        bpy.context.collection.objects.link(obj)

    apply_geonodes_modifier(obj, node_group)

    return obj


# ============================================================================
#  Резолвер: FULL (спавн с нуля) vs APPLY (кидаем на выделенные меши) ╰(*°▽°*)╯
# ============================================================================

def can_apply(generator_module, context) -> bool:
    """
    Заглушка для poll() в операторах. 
    Если генератор требует меш, проверяем, выделил ли юзер хоть один mesh-объект.
    """
    if getattr(generator_module, "REQUIRES_OBJECT", False):
        return any(obj.type == 'MESH' for obj in context.selected_objects)
    return True


def get_target_objects(generator_module, context, spawn_name: str = "FF_Object",
                        mod_name: str = "GeometryNodes"):
    """
    Главный маршрутизатор всей этой вечеринки.

    - Если генератор требует выделенный меш (REQUIRES_OBJECT = True, как у Blobs),
      то собираем все выделенные меши и вешаем на КАЖДЫЙ по модификатору.
    - Иначе (как с ромашками или травой) — не паримся, просто спавним 
      один новенький Empty и возвращаем его в списке.
      
    Минимум рутины, максимум автоматизации!
    """
    node_group = generator_module.create_node_group()

    if getattr(generator_module, "REQUIRES_OBJECT", False):
        selected = [obj for obj in context.selected_objects if obj.type == 'MESH']
        if not selected:
            return [], "Select at least one mesh object first"
        
        for obj in selected:
            apply_geonodes_modifier(obj, node_group, mod_name=mod_name)
        return selected, None

    return [spawn_object_with_geonodes(node_group, name=spawn_name)], None