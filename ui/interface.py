from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager 
from kivy.lang import Builder 

kv="""

GridLayout:
  cols:2
  TextInput:
  Button:
    on_press:app.diplay_value()
  Button:

"""


class Main(App):
    def build(self):
        return Builder.load_string(kv)
    def diplay_value(self):
        print("Value")
    
Main().run()