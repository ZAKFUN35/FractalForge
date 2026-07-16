"""
FF Blob Converter - Конвейер по производству стилизованных кустов ╰(*°▽°*)╯
Этот скрипт берет любую черновую геометрию (хоть дефолтный куб) и натягивает 
на нее процедурный модификатор "Блобов" из Geometry Nodes. 

Идеально для задников в стиле Ghibli, где нам не нужна проработка отдельных 
листьев (зачем убивать видеокарту тысячами билбордов на горизонте?), 
а важен только красивый, "мыльный" объем, который сэкономит нам заветные FPS.
"""

import bpy
from bpy.types import Operator
from ..nodes import blob
from ..nodes import bridge


class FF_OT_ConvertBlob(Operator):
    bl_idname = "ff.convert_blob"
    bl_label = "Превратить в блобы"
    bl_description = "Превращает любой Mesh-объект в процедурный кластер блобов"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # Защита от дурака. Проверяем через наш священный мост (bridge), 
        # выделил ли юзер вообще хоть один меш-объект. 
        # Не будем же мы натягивать геоноды на камеру или свет ¬_¬
        return bridge.can_apply(blob, context)

    def execute(self, context):
        # Главный триггер мутации. Запрашиваем у bridge нужные объекты 
        # и вешаем на них тяжелую артиллерию - "FF Blob Modifier".
        objects, error = bridge.get_target_objects(blob, context, mod_name="FF Blob Modifier")

        # Если юзер попытался обмануть систему и не выделил меш, ругаемся.
        if error:
            self.report({'WARNING'}, "Выберите хотя бы один Mesh-объект!")
            return {'CANCELLED'}

        # ОПТИМИЗАЦИЯ И ЗДРАВЫЙ СМЫСЛ:
        # Раньше скрипт жестко генерировал и назначал свой материал. 
        # Но зачем плодить новые датаблоки, если юзер уже мог заботливо 
        # повесить на болванку свой настроенный шейдер? 
        # 
        # Теперь сокет "Material" в геонодах остается пустым. Нода "Set Material" 
        # внутри графа просто игнорирует пустоту, и наш сгенерированный 
        # Ghibli-куст аккуратно наследует оригинальный материал объекта. 
        # Меньше мусора в аутлайнере - счастливее рендер ^_____^

        return {'FINISHED'}


classes = (FF_OT_ConvertBlob,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)