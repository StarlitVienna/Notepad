







from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.core.window import Window
from register_error import ErrorPopup
import bcrypt
import os
import sqlite3

Window.keyboard_anim_args = {"d":.2,"t":"linear"}
Window.softinput_mode = "below_target"



class RegisterPopup(Popup):
    def register_user(self):
        if self.ids.register_username.text == '' or self.ids.register_password.text == '' or len(self.ids.register_username.text) > 24:
            return
        conn = sqlite3.connect('./userNotes.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password BLOB NOT NULL)")

        hashed_password_to_register = bcrypt.hashpw(self.ids.register_password.text.encode('utf-8'), bcrypt.gensalt())
        username_to_register = self.ids.register_username.text

        try:
            c.execute("INSERT INTO user (username, password) VALUES (?,?)", (username_to_register, hashed_password_to_register))
        except:
            Factory.ErrorPopup().open()
            return 

        if os.path.isdir('./notes'):
            pass
        else:
            os.mkdir('./notes')

        
        os.mkdir(f'./notes/{username_to_register}')
        os.mkdir(f'./notes/{username_to_register}/main')

        conn.commit()
        conn.close()
        self.dismiss()

    pass
