






from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.popup import Popup
from kivy.clock import Clock
import load_everything
from functools import partial
import os
import main
import settings

global logged_user
logged_user = ""

class IconForListItem(OneLineIconListItem):
    icon = 'folder'

class CreateFolders(Popup):
    def create_folder(self):
        folder_name = self.ids.folder_name.text
        print(logged_user)
        if len(folder_name) > 100:
            return
        else:
            if os.path.isdir(f'./notes/{logged_user}/{folder_name}'):
                return
            else:
                os.mkdir(f'./notes/{logged_user}/{folder_name}')
                main.App.get_running_app().root.get_screen('FirstScreen').ids.folders_view.data.append(
                        {
                            'viewclass': 'IconForListItem',
                            'text': folder_name,
                            'on_release': partial(load_everything.Loader.load_drawer_folder, folder_name),
                            }
                        )
    pass

class DrawerContent():
    def __init__(self, **kwargs):
        global logged_user
        print(self)
        print(self)
        print(self)
        print(self)
        
        if logged_user != '':
            for i in os.listdir(f'./notes/{logged_user}/'):
        
                main.App.get_running_app().root.get_screen('FirstScreen').ids.folders_view.data.append(
                        {
                            'viewclass': 'IconForListItem',
                            'text': i,
                            'on_release': partial(load_everything.Loader.load_drawer_folder, i),
                            }
                        )


class Drawer(BoxLayout):

    def set_info(self):
        print(logged_user)
        print("yeppers")
    def open_settings(self):
        settings.SettingsScreen.configure_settings()
        main.App.get_running_app().root.current = 'settings'

    pass
