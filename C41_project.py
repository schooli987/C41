import requests
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog

API_KEY ="d0730148-3e9a-419f-80a2-ec1aa0077949"

class PlanetInfoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Dark"
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        self.input = MDTextField(
            hint_text="Enter planet name (e.g., mars)",
            size_hint_x=1
        )
        self.result = MDLabel(
            text="Planet info will appear here.",
            halign="center"
        )
        fetch_btn = MDRaisedButton(
            text="Get Info",
            on_release=self.fetch_planet_info,
            pos_hint={"center_x": 0.5}
        )

        layout.add_widget(self.input)
        layout.add_widget(fetch_btn)
        layout.add_widget(self.result)
        return layout

    def fetch_planet_info(self, *args):
        planet = self.input.text.strip().lower()
        if not planet:
            self.result.text = "Please enter a planet name."
            return

        url = f"https://api.le-systeme-solaire.net/rest.php/bodies/{planet}"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "application/json"
        }
        try:
            response = requests.get(url,headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                gravity = data.get('gravity', 'N/A')
                mass = data.get('mass', {}).get('massValue', 'N/A')
                moons = data.get('moons')
                if moons: 
                    moon_count = len(moons) 
                else:
                    moon_count = 0

                self.result.text = (
                    f"[u]{planet.capitalize()}[/u]\n"
                    f"Gravity: {gravity} m/s²\n"
                    f"Mass: {mass} x10²⁴ kg\n"
                    f"Moons: {moon_count}"
                )
                self.result.markup = True
            else:
                self.result.text = "Planet not found."
        except Exception as e:
            self.result.text = f"Error: {str(e)}"

if __name__ == "__main__":
    PlanetInfoApp().run()

