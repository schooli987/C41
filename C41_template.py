from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.image import AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
import requests


class MarsPhotoApp(MDApp):
    def build(self):
        self.title = "Mars Rover Photo Gallery"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.accent_palette = "Red"

        root = MDBoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))

        # Title and Subtitle
        title_label = MDLabel(
            text="[b]MARS ROVER PHOTO GALLERY[/b]",
            halign="center",
            markup=True,
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_color,
            font_style="H5",
            size_hint_y=None,
            height=dp(40)
        )

       
        # Top input layout
        top_box = MDBoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=dp(60))

        self.sol_input = MDTextField(
            hint_text="Enter a Mars sol (e.g., 1000)",
            mode="rectangle",
        
            text="1000",
            size_hint_x=0.7
        )
        search_btn = MDRaisedButton(
            text=" Search",
            size_hint_x=0.3,
           
        )
        top_box.add_widget(self.sol_input)
        top_box.add_widget(search_btn)

        # # Add widgets to root
        root.add_widget(title_label)
       
        root.add_widget(top_box)
        # root.add_widget(self.scroll)

        footer = FloatLayout(size_hint_y=None, height=dp(60))

        footer_content = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(4),  # very close spacing
            size_hint=(None, None),
            size=(dp(300), dp(40)),  # tighter size
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        nasa_logo = AsyncImage(
            source="nasa.png",
            size_hint=(None, None),
            size=(dp(30), dp(30)),
            allow_stretch=True
        )

        citation_label = MDLabel(
            text="Images courtesy of NASA's Mars Rover API",
            halign="left",
            theme_text_color="Hint",
            font_style="Caption",
            size_hint=(None, None),
            size=(dp(250), dp(30)),
            valign="middle"
        )

        footer_content.add_widget(nasa_logo)
        footer_content.add_widget(citation_label)
        footer.add_widget(footer_content)
        root.add_widget(footer)


        return root

    def fetch_mars_photos(self, instance):
       #fetch API here
        print("Write the function here")

MarsPhotoApp().run()
