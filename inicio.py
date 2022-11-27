from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
usuariopy = str(0)
contraseñapy = str(0)

class BoxLayoutExample(BoxLayout):
    pass
class BoxLayout1(BoxLayout):
    usuariopy = root.ids.contraseña_input.text
    contraseñapy = "0"

    def on_button_click(self,widget,widget2):
        print(widget.text + widget2.text)
        return [widget.text, widget2]

    usuario_0 = usuariopy
    contraseña_0 = contraseñapy

    pass

class BoxLayout2(BoxLayout):
    pass

class inicioApp(App):
    pass
usuario = BoxLayout1.usuario_0
inicioApp().run()
print(usuario)