
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDFloatingActionButton
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.utils import platform
import os
import threading
import time
import sys
App = MDApp

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])


Window.keyboard_anim_args = {'d': .1, 't': 'in_out_expo'}
Window.softinput_mode = 'below_target'

class ManageScreens(ScreenManager):
    def __init__(self, **kwargs):
        super(ManageScreens, self).__init__(**kwargs)

        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            current_screen = App.get_running_app().root.current
            
            if self.current_screen.name == 'editor' or self.current_screen.name == 'settings':
                self.current = 'FirstScreen'
                self.transition.direction = 'right'

        return True
    pass

class NoteIcon(OneLineIconListItem):
    icon = 'file-edit-outline'

class InitialScreen(Screen):
    pass

class FolderScreen(Screen):
    pass

class KivyApp(App):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        kv = Builder.load_file("./main.kv")
        return kv
    def build2(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"


if __name__ == '__main__':
    KivyApp().run()

