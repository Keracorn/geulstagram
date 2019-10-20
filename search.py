import pandas as pd
import random

def search(hashtag):
    df = pd.read_csv('/Users/hbae/Keracon/HashTag/Final_Data_v2_Cleansing_spell_checked_deleted.csv')
    count = df.shape[0]
    cc = 0
    list = []
    hashtag = "'" + hashtag + "'"

    for i in for i in range(count):
        text = df['Hashtags_result'][i]
        if hashtag in text:
            list.append(df['ID'][i])

    randomnum = random.randrange(1, len(list))
    index = randomnum % len(list)

    sentence = df['Spell_Checked_Content'][index]

    return sentence



