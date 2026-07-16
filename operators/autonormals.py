"""
FF AutoNormals - Наш главный инструмент для Ghibli-деревьев! 🌳
Этот скрипт решает проблему "радиоактивного брокколи" 
и жестких теней на листве. Он автоматически создает "мыльный" невидимый 
пузырь (fog proxy) вокруг каждого кластера листьев и копирует с него 
идеально мягкие нормали на нашу геометрию.
"""

import time
import bpy
from bpy.types import Operator

def _set_enum_safe(node, prop_name, candidates):
    """
    Защита от изменений API Блендера. 
    Ищет доступные варианты (enum) для ноды и ставит первый подошедший.
    Если Эпики или Блендер-фонд опять переименуют свойства под капотом - мы не упадем.
    """
    prop = node.bl_rna.properties.get(prop_name)
    valid = [item.identifier for item in prop.enum_items] if prop else []
    for c in candidates:
        if c in valid:
            setattr(node, prop_name, c)
            return c
    return None

def _find_socket(collection, candidates, fallback_index=None):
    """
    Еще один костыль безопасности. Ищем нужный пин (сокет) в ноде по списку имен.
    Если имя поменяли в новой версии - берем по запасному индексу.
    """
    for name in candidates:
        try:
            return collection[name]
        except KeyError:
            continue
    if fallback_index is not None:
        return collection[fallback_index]
    raise KeyError(f"none of {candidates} found in {[s.name for s in collection]}")

def _set_modifier_input(modifier, socket_name, value):
    """
    Функция-близнец из bridge.py! 
    Напоминалка: в Blender 5.2+ старый метод modifier["id"] = value тупо молчит 
    и ничего не делает. Поэтому мы лезем напрямую через properties.inputs.
    И да, не забываем передергивать show_viewport, иначе вьюпорт не обновится (⌐■_■)
    """
    ng = modifier.node_group
    if not hasattr(ng, "interface"):
        return False
    for item in ng.interface.items_tree:
        if getattr(item, "in_out", None) == "INPUT" and item.name == socket_name:
            socket = getattr(modifier.properties.inputs, item.identifier, None)
            if socket is not None and hasattr(socket, "value"):
                socket.value = value
                
                # Костыль для принудительного пересчета depsgraph'а
                modifier.show_viewport = False
                modifier.show_viewport = True
                return True
            return False
    return False

def _clear_custom_normals(obj):
    """
    ОЧЕНЬ ВАЖНАЯ МЕТЛА!
    Если мы нажмем кнопку авто-нормалей дважды, Блендер может сойти с ума 
    и запечь нормали поверх старых. Итог - черная, как смоль, листва (Black Mesh of Death).
    Поэтому перед работой мы жестко и безжалостно сносим старые кастомные нормали.
    """
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode="OBJECT")
    try:
        # Пытаемся удалить старым способом
        bpy.ops.mesh.customdata_custom_splitnormals_clear()
    except:
        pass
    
    # А тут добиваем новые атрибуты Блендера, чтобы наверняка
    attrs_to_remove = [
        attr.name for attr in obj.data.attributes 
        if "custom_normal" in attr.name.lower() or "split_normal" in attr.name.lower()
    ]
    for attr_name in attrs_to_remove:
        try:
            obj.data.attributes.remove(obj.data.attributes[attr_name])
        except:
            pass

def _create_perfect_blob_node_tree():
    """
    СЕРДЦЕ АДДОНА!
    Здесь мы генерируем нодовое дерево Geometry Nodes, которое превращает
    колючий куст листвы в идеально гладкий "блоб", чтобы украсть с него нормали.
    Ультимативный пайплайн: 
    Convex Hull -> Points/Volume -> Smooth -> Кража нормали!
    """
    ng = bpy.data.node_groups.new("_PerfectBlobNormal", "GeometryNodeTree")
    iface = ng.interface

    # Создаем входы для нашей нод-группы (настройки толщины, сглаживания и т.д.)
    iface.new_socket("Geometry", in_out="INPUT", socket_type="NodeSocketGeometry")
    iface.new_socket("Thickness", in_out="INPUT", socket_type="NodeSocketFloat").default_value = 0.05
    iface.new_socket("Smoothness", in_out="INPUT", socket_type="NodeSocketInt").default_value = 15
    iface.new_socket("Normal Blend", in_out="INPUT", socket_type="NodeSocketFloat").default_value = 1.0
    iface.new_socket("Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry")

    nodes = ng.nodes
    links = ng.links

    n_in = nodes.new("NodeGroupInput")
    n_out = nodes.new("NodeGroupOutput")

    # 1. Оболочка без дыр. Обтягиваем листья жесткой пленкой (как пищевой).
    hull = nodes.new("GeometryNodeConvexHull")
    links.new(_find_socket(n_in.outputs, ["Geometry"]), _find_socket(hull.inputs, ["Geometry"], 0))

    # 2. Подразделение. Добавляем полигонов, иначе оболочка будет угловатой, как в PS1.
    subdiv = nodes.new("GeometryNodeSubdivisionSurface")
    subdiv.inputs["Level"].default_value = 3
    links.new(_find_socket(hull.outputs, ["Convex Hull", "Geometry"], 0), _find_socket(subdiv.inputs, ["Mesh", "Geometry"], 0))

    # 3. Вершины в точки. Готовимся к магии вокселей.
    m2p = nodes.new("GeometryNodeMeshToPoints")
    m2p.mode = "VERTICES"
    links.new(_find_socket(subdiv.outputs, ["Mesh", "Geometry"], 0), _find_socket(m2p.inputs, ["Mesh", "Geometry"], 0))

    # 4. АВТО-МАСШТАБ 📏 (Чистый кайф!)
    # Чтобы не крутить радиус руками для каждого кустика, мы считываем 
    # Bounding Box (габариты меша) и вычисляем диагональ. 
    # Теперь туман сам подстраивается под масштаб ветки!
    bbox = nodes.new("GeometryNodeBoundBox")
    links.new(_find_socket(n_in.outputs, ["Geometry"]), _find_socket(bbox.inputs, ["Geometry"], 0))
    
    dist = nodes.new("ShaderNodeVectorMath")
    dist.operation = "DISTANCE"
    links.new(bbox.outputs["Min"], dist.inputs[0])
    links.new(bbox.outputs["Max"], dist.inputs[1])

    mul = nodes.new("ShaderNodeMath")
    mul.operation = "MULTIPLY"
    links.new(dist.outputs["Value"], mul.inputs[0])
    links.new(_find_socket(n_in.outputs, ["Thickness"]), mul.inputs[1])

    # 5. Точки в Объем (Volume). Делаем пушистое облачко! ☁️
    p2v = nodes.new("GeometryNodePointsToVolume")
    if hasattr(p2v, "resolution_mode"): p2v.resolution_mode = "VOXEL_AMOUNT"
    try: p2v.inputs["Voxel Amount"].default_value = 64
    except: pass
    links.new(_find_socket(m2p.outputs, ["Points"]), _find_socket(p2v.inputs, ["Points"], 0))
    links.new(mul.outputs["Value"], _find_socket(p2v.inputs, ["Radius"], 1))

    # 6. Объем обратно в меш. Воксельный Remesh прямиком в нодах.
    v2m = nodes.new("GeometryNodeVolumeToMesh")
    if hasattr(v2m, "resolution_mode"): v2m.resolution_mode = "VOXEL_AMOUNT"
    try: 
        v2m.inputs["Voxel Amount"].default_value = 64
        v2m.inputs["Threshold"].default_value = 0.1
    except: pass
    links.new(_find_socket(p2v.outputs, ["Volume"]), _find_socket(v2m.inputs, ["Volume"], 0))

    # 7. Блюр геометрии. Берем наш воксельный меш и сглаживаем его как утюгом.
    blur = nodes.new("GeometryNodeBlurAttribute")
    blur.data_type = "FLOAT_VECTOR"
    pos = nodes.new("GeometryNodeInputPosition")
    links.new(_find_socket(pos.outputs, ["Position"]), _find_socket(blur.inputs, ["Value"], 0))
    links.new(_find_socket(n_in.outputs, ["Smoothness"]), _find_socket(blur.inputs, ["Iterations"], 1))

    set_pos = nodes.new("GeometryNodeSetPosition")
    links.new(_find_socket(v2m.outputs, ["Mesh", "Geometry"], 0), _find_socket(set_pos.inputs, ["Geometry", "Mesh"], 0))
    links.new(_find_socket(blur.outputs, ["Value"]), _find_socket(set_pos.inputs, ["Position"], 2))

    # 8. Принудительный SHADE SMOOTH! 
    # Если этого не сделать, нормали считаются "лесенкой" с полигонов, и на листве будет грязь.
    smooth = nodes.new("GeometryNodeSetShadeSmooth")
    try: smooth.inputs["Shade Smooth"].default_value = True
    except: pass
    links.new(_find_socket(set_pos.outputs, ["Geometry", "Mesh"], 0), _find_socket(smooth.inputs, ["Geometry", "Mesh"], 0))

    # 9. КРАЖА НОРМАЛЕЙ (Собственно, ради чего всё затевалось) 🥷
    # Проецируем наши листики на этот идеальный "мыльный" пузырь и берем его нормали.
    sample = nodes.new("GeometryNodeSampleNearestSurface")
    sample.data_type = "FLOAT_VECTOR"
    links.new(_find_socket(smooth.outputs, ["Geometry"], 0), _find_socket(sample.inputs, ["Mesh", "Geometry"], 0))

    hull_norm = nodes.new("GeometryNodeInputNormal")
    links.new(_find_socket(hull_norm.outputs, ["Normal"]), _find_socket(sample.inputs, ["Value"], 1))

    # 10. Смешивание (Blend).
    # Оставляем юзеру возможность чуть-чуть подмешать оригинальные нормали,
    # если блоб сделал листву "слишком" круглой.
    orig_norm = nodes.new("GeometryNodeInputNormal")
    mix = nodes.new("ShaderNodeMix")
    mix.data_type = "VECTOR"
    links.new(_find_socket(n_in.outputs, ["Normal Blend"]), _find_socket(mix.inputs, ["Factor"]))
    links.new(_find_socket(orig_norm.outputs, ["Normal"]), _find_socket(mix.inputs, ["A"]))
    links.new(_find_socket(sample.outputs, ["Value"]), _find_socket(mix.inputs, ["B"]))

    # Нормализуем вектор (возвращаем длину к 1.0), чтобы шейдер в UE5 не сошел с ума
    norm_vec = nodes.new("ShaderNodeVectorMath")
    norm_vec.operation = "NORMALIZE"
    links.new(_find_socket(mix.outputs, ["Result"]), norm_vec.inputs[0])

    # 11. Записываем готовую идеальную нормаль обратно в меш! БАМ! 💥
    set_norm = nodes.new("GeometryNodeSetMeshNormal")
    if hasattr(set_norm, "mode"): set_norm.mode = "FREE"
    _set_enum_safe(set_norm, "domain", ["POINT", "VERTEX", "CORNER", "FACE_CORNER"])

    links.new(_find_socket(n_in.outputs, ["Geometry"]), _find_socket(set_norm.inputs, ["Mesh", "Geometry"], 0))
    links.new(norm_vec.outputs["Vector"], _find_socket(set_norm.inputs, ["Custom Normal", "Normal", "Vector"], -1))
    links.new(_find_socket(set_norm.outputs, ["Mesh", "Geometry"], 0), _find_socket(n_out.inputs, ["Geometry"], 0))

    return ng

def _process_island(island, node_tree, s):
    """
    Обрабатываем конкретный островок листвы.
    Вешаем на него наш модификатор PerfectBlob, передаем настройки из UI
    и сразу же применяем (apply), чтобы намертво зафиксировать кастомные нормали.
    """
    if len(island.data.vertices) == 0: return
    
    bpy.ops.object.select_all(action="DESELECT")
    island.select_set(True)
    bpy.context.view_layer.objects.active = island

    # На всякий случай включаем базовое сглаживание
    bpy.ops.object.shade_smooth()

    gn_mod = island.modifiers.new("PerfectBlob", "NODES")
    gn_mod.node_group = node_tree

    _set_modifier_input(gn_mod, "Thickness", s.thickness)
    _set_modifier_input(gn_mod, "Smoothness", s.smooth_iterations)
    _set_modifier_input(gn_mod, "Normal Blend", s.normal_strength)

    bpy.ops.object.modifier_apply(modifier="PerfectBlob")
    bpy.context.view_layer.update()


class FF_OT_AutoNormals(Operator):
    bl_idname = "ff.auto_normals"
    bl_label = "Авто-нормали листвы"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        foliage_obj = context.active_object
        
        # Проверка на дурака. Если юзер забыл выделить меш - ругаемся.
        if not foliage_obj or foliage_obj.type != "MESH":
            self.report({"ERROR"}, "Выдели меш листвы")
            return {"CANCELLED"}

        s = context.scene.ff_autonormals
        original_name = foliage_obj.name

        # Шаг 1: Сносим старые нормали, чтобы не получить черный артефакт
        _clear_custom_normals(foliage_obj)

        bpy.ops.object.select_all(action="DESELECT")
        foliage_obj.select_set(True)
        bpy.context.view_layer.objects.active = foliage_obj
        
        # Шаг 2: МЯСНИК В ДЕЛЕ! 🪓 
        # Разрубаем цельное дерево на независимые островки (кластеры).
        # Потому что нормали нужно считать для каждого пучка отдельно, а не для всей кроны разом.
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.mesh.separate(type="LOOSE")
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.context.view_layer.update()

        islands = [o for o in context.selected_objects if o.type == "MESH"]
        total = len(islands)
        if total == 0: return {"CANCELLED"}

        # Генерируем наше нодовое чудо всего один раз, чтобы сэкономить время
        node_tree = _create_perfect_blob_node_tree()

        # Красивый прогресс-бар внизу экрана, чтобы понимать, что аддон не завис
        wm = context.window_manager
        n_to_process = sum(1 for isl in islands if len(isl.data.vertices) > 0)
        wm.progress_begin(0, max(n_to_process, 1))

        empty_islands = []
        processed = 0
        t_start = time.time()
        
        # Шаг 3: Прогоняем каждый островок через конвейер
        for island in islands:
            # Иногда Separate by Loose Parts плодит пустые пустышки. Игнорируем их.
            if len(island.data.vertices) == 0:
                empty_islands.append(island)
                continue
            
            _process_island(island, node_tree, s)
            
            processed += 1
            wm.progress_update(processed)
            print(f"[FF AutoNormals] Обработан остров {processed}/{n_to_process}: {island.name}")

        wm.progress_end()
        total_time = time.time() - t_start
        print(f"[FF AutoNormals] Готово за {total_time:.2f} сек")

        # Шаг 4: Убираем за собой мусор (удаляем временную нод-группу и пустышки)
        bpy.data.node_groups.remove(node_tree)

        for empty in empty_islands:
            if empty in islands: islands.remove(empty)
            bpy.data.objects.remove(empty, do_unlink=True)

        if not islands: return {"CANCELLED"}

        # Шаг 5: Сшиваем всё обратно! 🧵
        # Берем все обработанные куски с крутыми нормалями и объединяем в один красивый меш.
        if len(islands) > 1:
            bpy.ops.object.select_all(action="DESELECT")
            for island in islands:
                island.select_set(True)
            bpy.context.view_layer.objects.active = islands[0]
            bpy.ops.object.join()
        else:
            bpy.context.view_layer.objects.active = islands[0]

        # Возвращаем оригинальное имя нашему Франкенштейну
        result_obj = context.view_layer.objects.active
        result_obj.name = original_name

        self.report({"INFO"}, f"Готово: {total} кластеров обработано за {total_time:.1f} сек ╰(*°▽°*)╯")
        return {"FINISHED"}


classes = (FF_OT_AutoNormals,)

def register():
    for cls in classes: bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes): bpy.utils.unregister_class(cls)