import pandas as pd
import random

def search():
    f = open('tag.txt', 'r')
    hashtag = f.readline()

    df = pd.read_csv('/Users/hbae/Keracon/HashTag/Final_Data_v2_Cleansing_spell_checked_deleted.csv')
    count = df.shape[0]
    cc = 0
    list = []
    hashtag = "'" + hashtag + "'"

    for i in range(count):
        text = df['Hashtags_result'][i]
        if hashtag in text:
            list.append(df['ID'][i])

    randomnum = random.randint(0, len(list))
    print(randomnum)
    index = list[randomnum]
    print(index)
    sentence = df['Spell_Checked_Content'][index]

    f.close()

    return sentence

sentence = search()
print(sentence)

