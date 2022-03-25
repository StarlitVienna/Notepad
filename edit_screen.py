








from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform
from kivymd.app import MDApp
#import login_popup
import main
import os


Window.keyboard_anim_args = {"d":.2,"t":"linear"}
Window.softinput_mode = "pan"



class Edit(Screen):
    global current_file
    global logged_user
    global current_folder
    current_file = ""
    current_folder = ""
    logged_user = ""


    def printer():
        edit_screen = main.App.get_running_app().root.get_screen('editor')

        print(edit_screen.ids.text_input.cursor_row)
        print(edit_screen.ids.text_input.line_height)
    def ontextil(self):
        print(Window.keyboard_height)
        print(platform)
        print('down')
        print(self.height + self.ids.text_input.line_height)
        print('up')
        print(f'selfish = {self.height}')
        number_of_rows_for_kheight = 0

        if platform=='android':
            from jnius import autoclass
            Activity = autoclass('org.kivy.android.PythonActivity')
            Rect = autoclass('android.graphics.Rect')
            root_window = Activity.getWindow()
            view = root_window.getDecorView()
            r = Rect()
            view.getWindowVisibleDisplayFrame(r)
            print(f'windowheight = {Window.height}')
            print(f'r.bottom = {r.bottom}')
            print(f'r.top = {r.top}')
            print(self.height)
            print (f' window height divided by self height = {Window.height/self.height}')
            print(f'heightttttt   |   {Window.height-(r.bottom-r.top)}')
            print(f'cursor row = {self.ids.text_input.cursor_row}')
            print(f'row height = {self.ids.text_input.line_height}')
            print(f'row*height = {self.ids.text_input.cursor_row*self.ids.text_input.line_height}')
            kheight = Window.height-(r.bottom-r.top)
            print(f"timers = {kheight*1.332874828060}")
            print(f'heightersssssssssssss = {int(self.ids.text_input.cursor_row*self.ids.text_input.line_height*0.75025799793)}')
            if int(self.ids.text_input.cursor_row*self.ids.text_input.line_height*0.75025799793) == kheight:
                number_of_rows_for_kheight = self.ids.text_input.cursor_row
                self.ids.text_input.height += self.ids.text_input.line_height
                self.ids.scroll.scroll_y = 0
        print(f'cursor row = {self.ids.text_input.cursor_row}')
        
        if self.ids.text_input.cursor_row >= 15:

            pass

    def scrollto(self):
        curx, cur_y = self.ids.text_input.cursor_pos
        cur_row = self.ids.text_input.cursor_row
        self.ids.scroll.scroll_y = (cur_row+.000001)






    def change_height(self):
        pass

    def style_editor(file, user, folder):
        global current_folder
        global current_file
        global logged_user
        edit_screen = main.App.get_running_app().root.get_screen('editor')
        
        current_folder = folder
        current_file = file
        logged_user = user
        edit_screen.ids.toolbar.title = file
        edit_screen.ids.toolbar.ids.label_title.halign = 'center'
        edit_screen.ids.toolbar.ids.label_title.color = (1,1,1,1)


        toolbar = edit_screen.ids.toolbar
    
        left_action_items = toolbar.ids.left_actions.children
        right_action_items = toolbar.ids.right_actions.children

        for item in left_action_items: item.text_color = (1,1,1,1)

        for item in right_action_items: item.text_color = (1,1,1,1)

        Edit.printer()

    def save_file(self, *args):
        with open(f"./notes/{logged_user}/{current_folder}/{current_file}", 'w') as f:
            f.write(self.ids.text_input.text)
            f.close()
        Edit.printer()
        pass

    def go_back(self, *args):
        main.App.get_running_app().root.transition.direction = 'right'
        main.App.get_running_app().root.current = 'FirstScreen'
        pass
    pass

