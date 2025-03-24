# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/as_merge_by_distance_msg

import blf
import bpy
from bpy.props import FloatProperty
from bpy.types import Operator, SpaceView3D
from bpy.utils import register_class, unregister_class
from functools import partial


class MERGE_BY_DISTANCE_MSG_OT_main(Operator):
    bl_idname = 'merge_by_distance_msg.main'
    bl_label = 'Merge by Distance Msg'
    bl_description = 'Merge by Distance with Message'
    bl_options = {'REGISTER', 'UNDO'}

    _handler = None     # flag for controlling currently showing message
    _msg_remove_ptr = None  # pointer on msg_remove function

    threshold: FloatProperty(
        name='threshold',
        default=0.0001,
        min=0
    )

    def execute(self, context):
        # vertices before merge
        bpy.context.object.update_from_editmode()
        vertices_before = len(context.object.data.vertices)
        # execute base merge
        bpy.ops.mesh.remove_doubles(
            threshold=self.threshold
        )
        # new count of vertices
        bpy.context.object.update_from_editmode()
        vertices_after = len(context.object.data.vertices)
        msg = f'Removed {vertices_before - vertices_after} vertices'
        # message
        self.msg_show(context=context, message=msg)
        return {'FINISHED'}

    @classmethod
    def msg_show(cls, context, message):
        # show message
        # first remove current message if exists
        cls.msg_remove(context=context)
        # show new message
        font_id = 0 # system font
        cls._handler = SpaceView3D.draw_handler_add(
            cls.draw_msg, (font_id, message), 'WINDOW', 'POST_PIXEL'
        )
        # redraw area
        cls.redraw_area(context=context)
        # timer for clearing message
        cls._msg_remove_ptr = partial(cls.msg_remove, context)
        bpy.app.timers.register(
            function=cls._msg_remove_ptr,
            first_interval=3
        )

    @classmethod
    def msg_remove(cls, context):
        # remove message
        if cls._handler:
            SpaceView3D.draw_handler_remove(cls._handler, 'WINDOW')
            bpy.app.timers.unregister(cls._msg_remove_ptr)
            cls._handler = None
            cls._msg_remove_ptr = None
        cls.redraw_area(context=context)

    @staticmethod
    def draw_msg(font_id, message):
        blf.position(font_id, 100, 150, 0)
        blf.size(font_id, 14)
        blf.color(font_id, 1.0, 1.0, 1.0, 1)
        blf.draw(font_id, message)

    @staticmethod
    def redraw_area(context):
        # redraw area
        for area in (_area for _area in bpy.context.screen.areas if _area.type == 'VIEW_3D'):
            area.tag_redraw()

    @classmethod
    def poll(cls, context):
        return True


def register():
    register_class(MERGE_BY_DISTANCE_MSG_OT_main)

def unregister():
    unregister_class(MERGE_BY_DISTANCE_MSG_OT_main)
