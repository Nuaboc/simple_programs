"""
Script to practice kivy for mobile development.

Tips from the following tutorials:

Python | ScreenManager in Kivy using .kv file
From Geek for Geeks, found in:
https://www.geeksforgeeks.org/python-screenmanager-in-kivy-using-kv-file/

Kivy Tutorial - Mobile App Development with Python
From Tech with Tim, found in:
https://www.techwithtim.net/tutorials/kivy-tutorial/multiple-screens/

Despite the >>PEP 8: E402<< says "module level import not at top of file"
for the kivy Config.set to affect the window, it should be imported and implemented
before importing other modules
"""

from kivy.config import Config
#Config.set('kivy', 'keyboard_mode', 'systemandmulti')
# Limit the resize option to be False
# Config.set('graphics', 'resizable', 0)
# The width nad height will be set as for an iphone 11R
# Fix the width of the window
# Config.set('graphics', 'width', 414)
# Fix the height of the window
# Config.set('graphics', 'height', 896)

# Now the rest of the modules may be imported
# Standard library imports
import time
import random

# Third party imports
from kivy.app import App
# from kivy.base import runTouchApp
# from kivy.uix.dropdown import DropDown
# from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
# Make available the Button class from the kivy library
from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.vkeyboard import VKeyboard

# import kivymd

# Local modules imports
# import func


class OpeningScreen(Screen):
    pass


class MainScreen(Screen):
    """dropdown = DropDown()
    for index in range(5):
        btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

        dropdown.add_widget(btn)"""
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__()
        self.pc = PopUpContent()
        self.p = Popup(title='Popup test', content=self.pc, size_hint=(None, None), size=(400, 400))
        self.prep_table()

    def prep_table(self):
        for i in range(1, 16):
            self.ids.container.add_widget(TextInput(text='slot ' + str(i), multiline=False))

    def press(self):
        print(self.test_var.text)
        # label = self.ids.test_var

    def show_keyboard(self):
        keys = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
                'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

        self.keyboard = StackLayout(pos_hint={'top': .25})
        x = 0

        for key in keys:
            btn = Button(text=key, width=40 + x * 5, size_hint=(None, 0.15))
            self.keyboard.add_widget(btn)
            x += 1

        self.add_widget(self.keyboard)


'''class CustomDropDown(DropDown):
    pass
'''


class Keyboard(VKeyboard):
    kb = VKeyboard()


class PopUpContent(FloatLayout):
    pass


class ColourScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])


class SettingsScreen(Screen):
    pass


class AboutScreen(Screen):

    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        #self.scroll()

    def scroll(self):
        lets_scroll = ScrollView(size_hint=(1, None), do_scroll_x=False, do_scroll_y=True)

        grid = GridLayout(col=3, size_hint_y=None)

        grid.bind(minimum_height=grid.setter("height"))

        for i in range(1, 50):
            grid.add_widget(Button(text="slot " + str(i), size_hint_y=None, height=40))

        lets_scroll.add_widget(grid)

        self.add_widget(lets_scroll)


# The ScreenManager controls moving between screens
class Root(ScreenManager):

    test_var = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.opening = OpeningScreen()

    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name, colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name

    def press(self):
        self.ids.test_var2 = test_var


class MobileApp(App):
    """A class to setup for the app basics."""

    def build(self):
        """This method will be used as a root for all widgets."""
        pass


if __name__ == "__main__":
    app = MobileApp()
    app.run()
