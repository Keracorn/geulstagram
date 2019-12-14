# HashTagBot

## HashTagBot 소개
2019년 케라스 공개 SW 컨트리뷰톤 프로젝트 중 하나인 `케라스 기반 챗봇 만들기`에 참가하여 **해시태그 기반으로 글을 생성해주는 챗봇**을 만들었습니다.

### 주요 기능
 * 챗봇에 해시태그를 적으면 사전에 수집한 데이터셋에서 랜덤으로 문장들을 뽑아줍니다.
 * 뽑힌 문장들은 번역 / 모델 등을 거쳐 새로운 문장으로 변형되어 챗봇의 아웃풋 값으로 반환됩니다.
 
### 개발 환경
개발 언어 : python <br>
모델 프레임 워크 : Keras  <br>
형태소 분석기 : Konlpy <br>


### 프로젝트 해시태그 구성원
*	__Mentee__ 
    *	__김우정__ [아주대학교 컴퓨터공학과 대학원생  _gks3284@ajou.ac.kr_]
    * __배현진__ [숙명여자대학교 IT공학전공 재학 _gloria9705@sookmyung.ac.kr_]
    * __안영진__ [연세대학교 Economics 학부생 young_ahn@yonsei.ac.kr]    
    * __백승주__ [아주대학교 산업공학과 / halucinor0@gmail.com]    
 *	__Mento__ 
    *	__김슬기 멘토님__ 
    

## 프로젝트 진행 과정

### 데이터셋 수집 
인플루엔서 리스트업 / 인스타 그램 게시글 크롤링 / 이미지 다운 으로 데이터셋을 수집하였습니다.

instagram crawler:
https://github.com/huaying/instagram-crawler

1. [게시글 작성자, 게시글 사진(jpg/png), 게시글 본문(string), 해시태그, 게시글 댓글] 정보를 담고 있는 json 파일을 생성
2. 해당 json 이미지 파일을 다운하고 Google Vision API를 사용하여 이미지 별 텍스트 추출
3. 최종 데이터 통합 (인스타그램 crawling 데이터 + 이미지로부터 OCR을 이용해 추출한 글 텍스트)

<USER_ID | CONTENT_ID | CONTENT_IMAGE_ID | Image_Content_txt | Content_txt | Hashtags>

4. 총 데이터 : 32,099, 동일 게시글 병합 : 25,196

* **ig_query_parser.py**
 : URL 상에서 유저의 아이디를 뽑아내는 소스코드
* **json_image_crawler.py**
 : json의 url을 통해 인스타 게시글 이미지를 다운로드 받는 소스코드
* **googleapi.py**
 : OCR을 작동시키는 소스
* **_human_parsing**
 : 게시글을 분석하여 json 파일을 만드는 소스코드

###  데이터 전처리 
* 이미지 콘텐츠 내에 해시태그가 걸려 있는 경우가 있어 유저 서명 삭제 처리를 하기 전에 제거해주었습니다.
* 유저가 쓴 글마다 유저의 필명 등이 서명처럼 들어가있습니다. 글의 앞부분이나 뒷부분에서 한 유저당 동일한 어절이 유저당 게시글의 50% 이상일 시 제거 처리해주었습니다. 서명이 두 어절 이상인 경우도 있어, 제거 요소가 나오지 않을 때까지 반복 처리해주었습니다.
* 동일한 해시태그가 모든 글에 반복적으로 등장하는 경우가 잦았습니다. 모든 유저의 해시태그 데이터를 카운트해 빈도수 1회이거나 최다 빈출 3개 이상인 태그는 제거해주었습니다.
* 맞춤법이 틀린 글은 검사하여 수정해주는 작업을 거쳤습니다. <br>
hanspell: https://github.com/ssut/py-hanspell/blob/master/README.md<br>
해당 맞춤법 검사기를 이용하여 추출된 이미지 텍스트의 맞춤법을 검사 <br>
맞춤법 검사는 py-hanspell 내부적으로 네이버 맞춤법 검사기를 사용


### 모델 생성

gpt2 colab
https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce

**Modeling**
 * RNN, Seq2Seq 자료조사
 * GPT-2를 이용한 생성 모델 학습 진행 중
 
**데이터 변형**
 * Translation (한글 →  다른 나라 언어 →  한글)
  * Google Translation API 이용

* **translateAPU.py**
 : 입력된 글을 영어로 번역한 뒤 한국어로 다시 번역해주는 코드

 * 명사 유의어로 변경하기 
    * Word2Vec

* **word2vec_train_and_save.py**
 : 사용자의 데이터를 학습해서 Word2Vec 모델로 반환해주는 코드
 * **word2vec_train_and_save.py**
 : Word2vec 모델을 이용해 받아낸 단어 별 유의어를 문장 내 모든 명사에 적용시켜 문장을 변형해주는 코드
 
## 참고 문헌

**NLP**
* BERT 세미나 자료: <https://www.slideshare.net/WonIkCho/1909-bert-whyandhow-code-seminar>
* 딥 러닝을 이용한 자연어 처리 입문: <https://wikidocs.net/book/2155>
* 쉽게 씌어진 Word2Vec: <https://dreamgonfly.github.io/machine/learning,/natural/language/processing/2017/08/16/word2vec_explained.html>

**데이터 수집**
* instagram-crawler: <https://github.com/huaying/instagram-crawler>
* Vision API Tutorial: <https://www.evernote.com/l/AZQhDK3EG1dPlYYGM7nz--qf_IpgswSIbQw/>

**데이터 전처리**
* han-spell: <https://github.com/ssut/py-hanspell/blob/master/README.md>

**모델링**
* gpt-2: <https://github.com/nshepperd/gpt-2>
* gpt-2 colab: <https://colab.research.google.com/github/ilopezfr/gpt-2/blob/master/gpt-2-playground_.ipynb?fbclid=IwAR21GZFZ2gWHFwZmWss5osQpxDRuZOQsx_RXdvSbBWbyTYBogYru9bRB6qY#scrollTo=_QIdaQn5WkSf>
