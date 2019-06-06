# Learning and testing Kivy framework

from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):
    """Testing the main window in kivy."""

    def build(self):
        """Don't know what this do."""
        return Label(text="Testing \n testing... \n 1...2...3")


if __name__ == "__main__":
    TestApp().run()
