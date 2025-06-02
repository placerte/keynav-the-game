from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#from kivy.uix.button import Button
from my_kivies import Button


class MyApp(App):

    button: Button

    def build(self):
        self.layout : BoxLayout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.button = Button(text="Click")
        self.button.bind(on_press=self.show_hello_world)
        self.layout.add_widget(self.button)
        return self.layout
    
    def show_hello_world(self, instance):
        self.label: Label = Label(text="Hello World!")
        self.layout.add_widget(self.label)

MyApp().run()

