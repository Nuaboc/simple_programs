"""
Tutorial for kivy BoxLayout.

Script from Real Python, found in:
https://realpython.com/mobile-app-kivy-python/
"""

import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


class HBoxLayoutExample(App):
    def build(self):
        # Create an instance of the boxlayout.
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            # Create an instance of >>Button()<< with some specific attributes and add it to the layout instance.
            btn = Button(text="Button #%s" % (i+1), background_color=random.choice(colors))
            layout.add_widget(btn)

        return layout


if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()
