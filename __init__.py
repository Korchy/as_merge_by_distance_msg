# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/as_merge_by_distance_msg

from . import merge_by_distance_msg_ops
from . import merge_by_distance_menu
from .addon import Addon


bl_info = {
    'name': 'Merge by Distance with Message',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (4, 4, 0),
    'location': '',
    'doc_url': 'https://github.com/Korchy/as_merge_by_distance_msg',
    'tracker_url': 'https://github.com/Korchy/as_merge_by_distance_msg',
    'description': 'Same as the base \"Merge by Distance\" operator but shows message on the 3D Viewport area'
}

def register():
    if not Addon.dev_mode():
        merge_by_distance_msg_ops.register()
        merge_by_distance_menu.register()
    else:
        print('It seems you are trying to use the dev version of the '
              + bl_info['name']
              + ' add-on. It may work not properly. Please download and use the release version')

def unregister():
    if not Addon.dev_mode():
        merge_by_distance_menu.unregister()
        merge_by_distance_msg_ops.unregister()

if __name__ == '__main__':
    register()
