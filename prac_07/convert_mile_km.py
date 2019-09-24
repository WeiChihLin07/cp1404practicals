"""
CP1404/CP5632 Practical - GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_mile_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation (could be button press or other call)."""
        print("handle_calculate")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        print("handle_increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)
        # Since the InputText.text has changed, its on_text event will fire and handle_calculate will be called

    def update_result(self, miles):
        print("update_result")
        self.output_km = str(miles * MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


MilesConverterApp().run()