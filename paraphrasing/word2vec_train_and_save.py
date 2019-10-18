import pandas as pd
import os

from konlpy.tag import Okt

## word2vec
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import word2vec

# load data
def load_data(PATH):
    data = pd.read_csv(PATH, index_col=1)
    data.columns = ['CONTENT_ID', 'USER_ID', 'Image_Content_txt',
                    'Image_Content_txt_result', 'Content_txt', 'Hashtags',
                    'Hashtags_result', 'Spell_Checked_Content']
    data = data.dropna(axis=0)
    data = data.reset_index(drop=True)

    return data

def tokenize_text(text):
    okt = Okt()
    malist = okt.pos(text,norm = True, stem = True)
    # [('칫솔', 'Noun'), ('은', 'Josa'), ('새다', 'Verb'), ('솔질', 'Noun')]
    r = []
    tag = ["Noun","Verb" ]
    try:
        for word in malist: # 형태소 분석 결과
            if word[1] in tag: # tag 에 있는 형태소만 받아내기
                if not word[0] in r: # 중복은 넣지 않음
                    r.append(word[0])
        return r
    except Exception as e:
        print (e)
        r.append(" ")

def tokenize_all(list2d_data):
    data_tokens = []
    for i, txt in enumerate(list2d_data):
        print("'\r{0}%".format(i/len(list2d_data)*100), end='')
        data_tokens.append(tokenize_text(txt))
    print(data_tokens[:3], end='')

    return data_tokens
    # [['칫솔', '새다', '솔질', '잇몸', '피', '나다', '저', '뺏뻣', '것', '벌어지다', '솔', '문지르다', '조만간', '꼴다', '하다', '않다'],
    #  ['아무', '않다', '요즘', '미우다', '것', '벗', '더', '사이'],
    #  ['어제', '초승', '것', '오늘', '보름', '이겠다', '만', '너', '밤하늘', '빛', '달', '벌써', '가득', '보다', '가장', '크다']]


def comment_count(token_data):
    unique_comment_tokenized = [list(i) for i in set(tuple(i) for i in token_data)]
    word_dic = {}

    # word count
    for words in unique_comment_tokenized:
        for word in words:
            if not (word in word_dic):
                word_dic[word] = 0
            word_dic[word] += 1

    keys = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
    for word, count in keys[:100]:  # 상위 백 개 뽑기
        print("{0}({1}) ".format(word, count), end="")

    # [] 없애주는 코드
    from itertools import chain
    words = set(chain(*unique_comment_tokenized))

    n_vocab = len(words)
    print("\n")
    print("Total Vocab: ", n_vocab)

    return keys, n_vocab


if __name__ == '__main__':
    print("데이터 불러오기")
    data = load_data('Final_Data_v2_Cleansing_v2_spell_checked.csv')
    print("데이터 불러오기 완료")

    # tokenize  total data
    print("데이터 토큰화 하기")
    data_tokens = tokenize_all(data['Spell_Checked_Content'])
    print("데이터 토큰화 완료")

    # count unique token
    #K = comment_count(data_tokens)

    # train and save model

    config = {
        'min_count': 2,  # 등장 횟수가 2 이하인 단어는 무시
        'size': 300,  # n차원짜리 벡터스페이스에 embedding
        'sg': 1,  # 0이면 CBOW, 1이면 skip-gram을 사용한다
        'batch_words': 10000,  # 사전을 구축할때 한번에 읽을 단어 수
        'iter': 1000,  # 보통 딥러닝에서 말하는 epoch과 비슷한, 반복 횟수
        'workers': 4, #cpu thread
    }

    print('word2vec 모델 만들기 학습하기')
    model = word2vec.Word2Vec(data_tokens, **config)  # skip-gram model
    model.save("paraphrasing/gamsung_txt.model")
    print('word2vec 모델 저장 완료')
