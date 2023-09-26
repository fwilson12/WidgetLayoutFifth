from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class WidgetLayoutApp(App):
    pass

class StackLayoutExample(StackLayout):
    pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'lr-tb'
        for letter in 'qwertyuiopasdfghjklzxcvbnm0123456789':
            b = Button(text= letter, size_hint=(.15,.15))
            self.add_widget(b)


class LayoutAssignment(BoxLayout):
    pass




class GridLayoutExample(GridLayout):
    pass

WidgetLayoutApp().run()
