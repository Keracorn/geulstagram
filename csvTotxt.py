import pandas as pd
from google.cloud import translate
import os
import numpy as np
import csv

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/Users/hbae/PycharmProjects/keraconocr/venv/credentials2.json'


def test():
    df = pd.read_csv('/Users/hbae/PycharmProjects/keraconocr/venv/Final_Data_v2_Cleansing_spell_checked_deleted.csv')
    #print(df['Image_Content_txt'][0])
    count = df.shape[0]


    file=open("/Users/hbae/PycharmProjects/keraconocr/venv/translated.csv", 'w', newline='', encoding='utf-8-sig')

    wr = csv.writer(file)
    header = ["ID", "번역"]
    wr.writerow(header)


    for i in range(count):
        text = df['Spell_Checked_Content'][i]
        print(text)
        translated = str(translate_text(text))
        list = [i, translated]
        print(translated)
        wr.writerow(list)


    file.close()

# 번역
def translate_text(text):
    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    #text = u'Hello, world!'

    # The target language
    target = 'en'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    translated_text = translation['translatedText']

    return translated_text

    #print(u'Target Lang: {}'.format(target))
    #print(u'Text: {}'.format(text))
    #print(u'Translation: {}'.format(translation['translatedText']))

#번역한거랑 전체데이터 합쳐주는 함수
def merge():
    b = pd.read_csv("/Users/hbae/PycharmProjects/keraconocr/venv/translated.csv")
    a = pd.read_csv("/Users/hbae/PycharmProjects/keraconocr/venv/Final_Data_Cleansing_v2 복사본.csv")

    a.rename(columns={'Unnamed: 0':'ID'}, inplace = True)
    b.rename(columns={'번': 'ID'}, inplace=True)
    print(a.columns.values[0])
    merged = a.merge(b, on='ID')
    print(merged)
    merged.to_csv("/Users/hbae/PycharmProjects/keraconocr/venv/output.csv", index=False)

#nan 포함된 행 없애주는 함수
def delete():
    df = pd.read_csv('/Users/hbae/PycharmProjects/keraconocr/venv/Final_Data_v2_Cleansing_v2_spell_checked.csv')
    df = df.dropna(axis=0)
    df.to_csv('/Users/hbae/PycharmProjects/keraconocr/venv/Final_Data_v2_Cleansing_spell_checked_deleted.csv', index=False)


if __name__ == '__main__':
    test()