





from kivy.uix.popup import Popup
from kivy.core.window import Window
import login_popup
import main
from functools import partial
from edit_screen import Edit
import os

Window.keyboard_anim_args = {'d': .1, 't': 'in_out_expo'}
Window.softinput_mode = 'below_target'

global current_folder
current_folder = ""

def change_screen(file):
    global current_folder
    user = login_popup.logged_user
    edit_screen = main.App.get_running_app().root.get_screen('editor')
    if current_folder == "":
        current_folder = "main"
    with open(f"./notes/{user}/{current_folder}/{file}", 'r') as f:
        edit_screen.ids.text_input.text = f.read().strip()
        f.close()
    
    Edit.style_editor(file, user, current_folder)

    main.App.get_running_app().root.transition.direction = 'left'
    main.App.get_running_app().root.current = 'editor'



class test:
    def ok():
        print('ok')
class NewFile(Popup):
    
    def save_file(self):
        global current_folder
        logged_user = login_popup.logged_user
        if current_folder == "":
            current_folder = "main"

        for i in os.listdir(f"./notes/{logged_user}/{current_folder}/"):
            if self.ids.file_name.text == i:
                return
        os.mknod(f'./notes/{logged_user}/{current_folder}/{self.ids.file_name.text}')
        main.App.get_running_app().root.get_screen('FirstScreen').ids.rv.data.append(
                    {
                        'viewclass': "NoteIcon",
                        'text': str(self.ids.file_name.text),
                        'on_release': partial(change_screen, str(self.ids.file_name.text)),
                        }
                    )

        self.dismiss()
        pass
    pass
