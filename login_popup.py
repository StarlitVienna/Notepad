from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.properties import StringProperty
import drawer_window
from register import RegisterPopup
import searcher
import main
import load_everything
import os
import bcrypt
import sqlite3
Window.keyboard_anim_args = {'d': .1, 't': 'in_out_expo'}
Window.softinput_mode = 'below_target'

a = "a"
logged_user = ""
hashedpass = None

class LoginPopup(Popup):
    def login(self):
        global logged_user
        global hashedpass
        self.ids.login_button.disabled = True


        conn = sqlite3.connect('userNotes.db')
        c = conn.cursor()
        try:
            c.execute(f"SELECT password FROM user WHERE username=?", [self.ids.username.text])
        except:
            self.ids.login_button.disabled = True

        for i in c.fetchall():
            if bcrypt.checkpw(self.ids.password.text.encode('utf-8'), i[0]):
                logged_user = self.ids.username.text
                logged_user_property_for_drawer = self.ids.username.text
                hashedpass = i[0]


                main_screen = main.App.get_running_app().root.get_screen('FirstScreen')
                main_screen.remove_widget(main.App.get_running_app().root.get_screen('FirstScreen').ids.login)
                main_screen.ids.user_label.text = logged_user

                def show_buttons():
                    ids = main_screen.ids
                    
                    ids.create_folders.opacity = 1
                    ids.create_folders.disabled = False
                    
                    ids.delete_button.opacity = 1
                    ids.delete_button.disabled = False
                    
                    ids.edit_button.opacity = 1
                    ids.edit_button.disabled = False

                
                show_buttons()

                load_everything.Loader(logged_user)
                drawer_window.logged_user = logged_user
                drawer_window.DrawerContent()

                searcher.logged_user = logged_user


            else:
                self.ids.login_button.disabled = False

                return
        self.ids.login_button.disabled = False

        conn.close()
    def register_popup(self):
        return Factory.RegisterPopup().open()
    pass
