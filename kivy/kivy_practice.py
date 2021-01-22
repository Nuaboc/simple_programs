# Learning and testing Kivy framework

from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):
    """Testing the main window in kivy."""

    def build(self):
        """ build() needs to be overwritten """
        # One of the >>Label<< attributes is >>text<<
        # parameters size_hint and pos_hint has default values
        return Label(text="Testing \n testing... \n 1...2...3")


if __name__ == "__main__":
    TestApp().run()
