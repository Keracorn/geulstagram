#AIzaSyDxywTKCFBM2oHFstLGQrRH8AYl77uIZTM
import os


# Imports the Google Cloud client library
from google.cloud import translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'credentials2.json'

def translate_word(text):
    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    #text = u'Hello, world!'
    #text = input(u"번역할 글을 입력해주세요: ")

    # The target language
    target = 'en'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    #print(u'Target Lang: {}'.format(target))
    #print(u'Text: {}'.format(text))
    #print(u'Translation: {}'.format(translation['translatedText']))


    # 글 역번역하기(일 -> 한)
    # The text to translate
    text2 = translation['translatedText']

    # The target language
    target2 = 'ko'

    # Translates some text into Russian
    translation2 = translate_client.translate(
        text2,
        target_language=target2)

    translated_word = translation2['translatedText']

    return translated_word
    #print(u'Text: {}'.format(text2))
    #print(u'Translation: {}'.format(translated_word))
    #print(u'Checked: {}'.format(spellcheck(translated_word)))
