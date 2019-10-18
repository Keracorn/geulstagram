## word2vec
from gensim.models import word2vec
## konlpy
from konlpy.tag import Okt
okt = Okt()

import pandas as pd

# load data
def load_data(PATH):
    data = pd.read_csv(PATH, index_col=1)
    data.columns = ['CONTENT_ID', 'USER_ID', 'Image_Content_txt',
                    'Image_Content_txt_result', 'Content_txt', 'Hashtags',
                    'Hashtags_result', 'Spell_Checked_Content']
    data = data.dropna(axis=0)
    data = data.reset_index(drop=True)

    return data


def most_similar_word(word):
    sim_result = word2vecModel.wv.most_similar(word)  # 유사한 순서대로 단어, 퍼센트 출력
    for sim_word, sim_pct in sim_result:
        if okt.pos(word)[0][1] == okt.pos(sim_word)[0][1]:  # 형태소 성분이 같으면 반환
            return sim_word

def change_word(txt):
    ch_txt = txt
    for word,tag in okt.pos(ch_txt):#,stem=True):
        if tag == 'Noun':
            try:
                ch_txt = ch_txt.replace(word,most_similar_word(word))
            except (KeyError,TypeError):
                # key error : model에 vocab이 없음, type error : similar word가 없음
                continue
    print("before:",txt,"\nChanged:", ch_txt)
    print()
    return ch_txt


if __name__ == '__main__':
    print("데이터 및 모델 불러오기")
    data = load_data('Final_Data_v2_Cleansing_v2_spell_checked.csv')
    word2vecModel = word2vec.Word2Vec.load("paraphrasing/gamsung_txt.model")  # 저장한 워드투벡 모델 불러오기
    print("불러오기 완료")
    print("텍스트 변형 적용")
    data['Change_word_2_sim'] = data['Spell_Checked_Content'].apply(change_word)



