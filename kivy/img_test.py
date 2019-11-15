from kivy.app import App
from kivy.uix.image import Image


class TestApp(App):
    """"""

    def build(self):
        img = Image(source='images/python_bg.png',
                    size_hint=(1, 1),
                    pos_hint={'center_x':.5, 'center_y':.5})

        return img


if __name__ == '__main__':
    app = TestApp()
    app.run()
