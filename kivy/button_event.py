"""
Tutorial for kivy button event.

Script from Real Python, found in:
https://realpython.com/mobile-app-kivy-python/
"""

from kivy.app import App
from kivy.uix.button import Button


class MainApp(App):

    def build(self):
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})

        # Connect the button press with a specific action
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        print('You pressed the button!')


if __name__ == '__main__':
    app = MainApp()
    app.run()
