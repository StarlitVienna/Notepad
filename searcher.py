




from kivymd.uix.textfield import MDTextField
import main
from functools import partial
import os
from edit_screen import Edit
class Search(MDTextField):
    global current_folder
    global logged_user
    current_folder = ""
    logged_user = ""
    
    def searching(text="", search = False):
        global current_folder
        global logged_user


        main_screen = main.App.get_running_app().root.get_screen('FirstScreen')
        def change_screen(file):
            global current_folder
            global logged_user

            edit_screen = main.App.get_running_app().root.get_screen('editor')
            with open(f"./notes/{logged_user}/{current_folder}/{file}", 'r') as f:
                edit_screen.ids.text_input.text = f.read().strip()
                f.close()
            Edit.style_editor(file, logged_user, current_folder)
            main.App.get_running_app().root.transition.direction = 'left'
            main.App.get_running_app().root.current = 'editor'

        if search == True:
            main_screen.ids.rv.data = []
            for notes in os.listdir(f"./notes/{logged_user}/{current_folder}"):

                if text in notes:
                    main_screen.ids.rv.data.append(
                            {
                        'viewclass': "NoteIcon",
                        'text': str(notes),
                        'on_release': partial(change_screen, str(notes)),

                                }
                            )


