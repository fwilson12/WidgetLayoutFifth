from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget



class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class WidgetLayoutApp(App):
    pass

class StackLayoutExample(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'lr-tb'
        cb = Button(text='Crazy Button',size_hint='.5,.5')

WidgetLayoutApp().run()


