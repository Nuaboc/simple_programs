"""
Tutorial for kivy button event with Kv language applied.

Script from Real Python, found in:
https://realpython.com/mobile-app-kivy-python/
"""

from kivy.app import App
from kivy.uix.button import Button


class ButtonApp(App):

    def build(self):
        return Button()

    def on_press_button(self):
        print('You pressed the button!')


if __name__ == '__main__':
    app = ButtonApp()
    app.run()
