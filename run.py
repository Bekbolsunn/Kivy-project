from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config

# Config.set("graphics", "resizable", 0)
# Config.set("graphics", "width", 700)
# Config.set("graphics", "height", 500)

class Aplication(App):

    def click(self, instance):
        self.label.text = "Thank's"

    def build(self):

        but_together = BoxLayout()
        grid = GridLayout(cols=1)

        my_but = Button(text="Click me please !", font_size=30, background_color="cyan", on_press=self.click)
        think_of_name = Button(text="Don't click me !", font_size=30, background_color="red")
        self.label = Label(text="This text", font_size=30)

        but_together.add_widget(my_but)
        but_together.add_widget(think_of_name)

        grid.add_widget(self.label)
        grid.add_widget(but_together)

        return grid


if __name__ == "__main__":
    Aplication().run()
