from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from my_kivies import Button
from kivy.uix.floatlayout import FloatLayout
from game_logic import Game

class MyApp(App):

    button: Button
    layout: FloatLayout
    button_rel_pos: tuple[float, float] = (0.5,0.5)
    game: Game = Game()
    score_label: Label

    def build(self):
        self.layout= FloatLayout()
        self.build_button()
        self.build_score_label()
        #TODO verify if it is required
        Window.bind(on_resize=lambda *_: self.place_button())
        Window.fullscreen = 'auto'
        return self.layout
    
    #TODO verify it is required
    def on_start(self):
        self.place_button()

    def build_score_label(self):
        self.score_label = Label()
        self.layout.add_widget(self.score_label)



    def build_button(self):
        self.button = Button(text="Click")
        self.button.size_hint = (None, None)
        self.button.size = (220, 160)
        self.place_button()
        self.button.bind(on_press=self.move_button)
        self.layout.add_widget(self.button)
    
    def move_button(self, instance):
        self.game.register_click()
        self._update_score_label()
        self.game.choose_next_position()
        self.place_button()


    def place_button(self, clamp_to_bounds: bool = True):
        x_rel, y_rel = self.game.button_relative_position
        x: int = int(Window.width* x_rel - (self.button.width/2))
        y: int = int(Window.height* y_rel - (self.button.height/2))

        self.button.pos = (x,y)

        if clamp_to_bounds:
            self._clamp_to_bounds()

    def _clamp_to_bounds(self):

        current_x, current_y = self.button.pos
        new_x: int = current_x
        new_y: int = current_y
        max_x, max_y = Window.size

        if current_y < 0:
            new_y = 0

        if current_y + self.button.height > max_y:
            new_y = max_y - self.button.height

        if current_x < 0:
            new_x = 0

        if current_x + self.button.width > max_x:
            new_x = max_x - self.button.width

        self.button.pos = (new_x, new_y)

    def _update_score_label(self):
        self.score_label.text = self.game.score_string

MyApp().run()

