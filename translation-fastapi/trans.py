from googletrans import Translator

def translate_to_spanish(english_text):
    translator = Translator()
    spanish_text = translator.translate(english_text, src='en', dest='es').text
    return spanish_text


