from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from my_kivies import Button
from kivy.uix.floatlayout import FloatLayout
import numpy as np

class MyApp(App):

    button: Button
    layout: FloatLayout
    button_rel_pos: tuple[float, float] = (0.5,0.5)

    def build(self):
        self.layout= FloatLayout()
        self.build_button()
        return self.layout

    def build_button(self):
        self.button = Button(text="Click")
        self.button.size_hint = (None, None)
        self.button.size = (220, 160)
        self.place_button()
        self.button.bind(on_press=self.move_button)
        self.layout.add_widget(self.button)
    
    def move_button(self, instance):
        self.choose_next_position()
        self.place_button()

    def choose_next_position(self):
        x: float = np.random.random() 
        y: float = np.random.random() 

        self.button_rel_pos = (x,y)

    def place_button(self):
        x_rel, y_rel = self.button_rel_pos
        x: int = int(Window.width* x_rel - (self.button.width/2))
        y: int = int(Window.height* y_rel - (self.button.height/2))

        self.button.pos = (x,y)

    def show_hello_world(self, instance):
        self.label: Label = Label(text="Hello World!")
        self.layout.add_widget(self.label)

MyApp().run()

