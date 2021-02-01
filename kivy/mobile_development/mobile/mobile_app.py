"""
Script to practice kivy for mobile development.

Tips from the following tutorials:

Python | ScreenManager in Kivy using .kv file
From Geek for Geeks, found in:
https://www.geeksforgeeks.org/python-screenmanager-in-kivy-using-kv-file/

Kivy Tutorial - Mobile App Development with Python
From Tech with Tim, found in:
https://www.techwithtim.net/tutorials/kivy-tutorial/multiple-screens/

Tutorial of a calculator with Kivy.
From Real Python, found in:
https://realpython.com/mobile-app-kivy-python/
"""

# Despite the >>PEP 8: E402<< says "module level import not at top of file"
# for the kivy Config.set to affect the window, it should be imported and implemented
# before importing other modules
from kivy.config import Config
# Limit the resize option to be False
Config.set('graphics', 'resizable', 0)
# The width nad height will be set as for an iphone 11R
# Fix the width of the window
Config.set('graphics', 'width', 414)
# Fix the height of the window
Config.set('graphics', 'height', 896)

# Now the rest of the modules may be imported
# Standard library imports
import random

# Third party imports
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
# Make available the Button class from the kivy library
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

import time
import random


class OpeningScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class Table(GridLayout):

    def __init__(self, **kwargs):
        super(Table, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 3

        self.add_widget(Label(text='First: '))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='Last: '))
        self.last = TextInput(multiline=False)
        self.add_widget(self.last)

        self.add_widget(Label(text='Email: '))
        self.mail = TextInput(multiline=False)
        self.add_widget(self.mail)


class PopUpScreen(Screen):
    pass


class ColourScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])


class SettingsScreen(Screen):
    pass


# The ScreenManager controls moving between screens
class Root(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.opening = OpeningScreen()

    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name, colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name

    def go_to_settings_screen(self):
        settings = SettingsScreen()
        self.add_widget(settings)


class MobileApp(App):
    """A class to setup for the app basics."""

    def build(self):
        """This method will be used as a root for all widgets."""
        pass


if __name__ == "__main__":
    app = MobileApp()
    app.run()
