#AIzaSyDxywTKCFBM2oHFstLGQrRH8AYl77uIZTM
import os


# Imports the Google Cloud client library
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'

def translate_word_eng(text):
    # Instantiates a client
    translate_client = translate.Client()

    # The target language
    target = 'en'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    translated_word = translation['translatedText']



    return translated_word

def translate_word_kor(text):
    # Instantiates a client
    translate_client = translate.Client()

    # The target language
    target = 'ko'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    translated_word = translation['translatedText']



    return translated_word