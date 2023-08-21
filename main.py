
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout



class Ui (ScreenManager):
    pass
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette ='Teal' # para ver el color de fondo 
        Builder.load_file('design.kv')

        return Ui()
    
    def change_style(self, checked, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'
        


if __name__== "__main__":
    MainApp().run()
    
