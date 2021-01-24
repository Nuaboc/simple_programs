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
import random
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
# Make available the Button class from the kivy library
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MainScreen(Screen):
    pass


class PopUpScreen(Screen):
    pass


# The ScreenManager controls moving between screens
screen_manager = ScreenManager()


class MobileApp(App):
    """A class to setup the app basics."""

    def build(self):
        """This method will be used as a root for all widgets."""
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical", padding=10)
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (
                    self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MobileApp()
    app.run()
