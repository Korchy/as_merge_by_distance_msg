# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/as_merge_by_distance_msg

from bpy.app.handlers import persistent
from bpy.types import VIEW3D_MT_edit_mesh_merge

@persistent
def merge_by_distance_msg_menu_func(self, context):
    self.layout.operator('merge_by_distance_msg.main', text='By Distance Msg')

def register():
        VIEW3D_MT_edit_mesh_merge.append(merge_by_distance_msg_menu_func)

def unregister():
        VIEW3D_MT_edit_mesh_merge.remove(merge_by_distance_msg_menu_func)

if __name__ == '__main__':
    register()
