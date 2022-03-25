





from kivy.uix.screenmanager import Screen
from functools import partial
import main


class SettingsScreen(Screen):
    global is_settings_loaded
    is_settings_loaded = False
    def configure_settings():
        global is_settings_loaded

        toolbar = main.App.get_running_app().root.get_screen('settings').ids.toolbar
        toolbar.ids.label_title.text_color = (1,1,1,1)
        left_action_items = toolbar.ids.left_actions.children
        right_action_items = toolbar.ids.right_actions.children


        for i in left_action_items: i.text_color= (1,1,1,1)
        for i in right_action_items: i.text_color= (1,1,1,1)

        settings_screen = main.App.get_running_app().root.get_screen('settings')
        dict1 = {
                'text': ['Font size', 'Theme', 'Button color', 'Icons color']
                }
        if is_settings_loaded == False:
            for i in dict1['text']:
                print(i)
                print('yeppers>>>')
                settings_screen.ids.settings_options.data.append(
                        {
                            'viewclass': 'OneLineListItem',
                            'text': i,
                            'on_release': partial(print, i)
                            }
                        )
            is_settings_loaded = True
    def default_options(self, *args):
        pass

    def go_back(self, *args):
        main.App.get_running_app().root.current = 'FirstScreen'
    pass
