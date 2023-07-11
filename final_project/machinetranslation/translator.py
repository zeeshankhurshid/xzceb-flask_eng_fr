# pylint: disable=missing-module-docstring
from deep_translator import MyMemoryTranslator
def english2_french(english_text):
    french_text = MyMemoryTranslator(source="en-IN", target="fr-FR").translate(english_text)
    return french_text
def french2_english(french_text):
    english_text = MyMemoryTranslator(source="fr-FR", target="en-IN").translate(french_text)
    return english_text
