






#import login_popup
import main
import os
from functools import partial
from edit_screen import Edit
import create_file_popup
import searcher

global logged_user
logged_user = ""
class Loader():

    def change_screen(self, file, folder):
        edit_screen = main.App.get_running_app().root.get_screen('editor')

        with open(f"./notes/{logged_user}/{folder}/{file}", 'r') as f:
            edit_screen.ids.text_input.text = f.read().strip()
            f.close()
        Edit.style_editor(file, logged_user, folder)

        main.App.get_running_app().root.transition.direction = 'left'
        main.App.get_running_app().root.current = 'editor'

    def __init__(self, user):
        global logged_user
        logged_user = user
        searcher.current_folder = 'main'



        for i in os.listdir(f'./notes/{user}/main/'):
            main.App.get_running_app().root.get_screen('FirstScreen').ids.rv.data.append(
                    {
                        'viewclass': "NoteIcon",
                        'text': str(i),
                        'on_release': partial(self.change_screen, str(i), "main")
                        }
                    )
    def load_drawer_folder(folder):
        main_screen = main.App.get_running_app().root.get_screen('FirstScreen')
        main_screen.ids.rv.data = {}
        create_file_popup.current_folder = folder
        searcher.current_folder = folder

        for i in os.listdir(f"./notes/{logged_user}/{folder}"):
            main_screen.ids.rv.data.append(
                    {
                        'viewclass': 'NoteIcon',
                        'text': i,
                        'on_release': partial(Loader.change_screen, None, i, folder),
                        }
                    )


