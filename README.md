# HashTagBot
---
## HashTagBot 소개
2019년 케라스 공개 SW 컨트리뷰톤 프로젝트 중 하나인 `케라스 기반 챗봇 만들기`에 참가하여  해시태그 기반으로 글을 생성을 해주는 챗봇을 만들었습니다.

### 주요 기능
 * 챗봇에 해시태그를 적으면 사전에 수집한 데이터셋에서 랜덤으로 문장들을 뽑아줍니다.
 * 뽑힌 문장들은 번역 / 모델 등을 거쳐 새로운 문장으로 변형되어 챗봇의 아웃풋 값으로 반환됩니다.
 
### 개발 환경
개발 언어 : python
모델 프레임 워크 : Keras
형태소 분석기 : Konlpy


 ### 프로젝트 해시태그 구성원
 *	__Mento__ 
    *	__김슬기 멘토님__ 
*	__Mentee__ 
    *	__김우정__ [아주대학교 컴퓨터공학과 대학원생  _gks3284@ajou.ac.kr_]
    *	__이름__ [간단한 소개 _메일_]	

---
## 프로젝트 진행 과정

### 데이터셋 수집 
 인플루엔서 리스트업 / 인스타 그램 게시글 크롤링 / 이미지 다운 으로 데이터셋을 수집하였습니다.
 
 1. [게시글 작성자, 게시글 사진(jpg/png), 게시글 본문(string), 해시태그, 게시글 댓글] 정보를 담고 있는 json 파일을 생성
 2. 해당 json 이미지 파일을 다운하고 Google Vision API를 사용하여 이미지 별 텍스트 추출
 3. 최종 데이터 통합 (인스타그램 crawling 데이터 + 이미지로부터 OCR을 이용해 추출한 글 텍스트)
 
    **<USER_ID | CONTENT_ID | CONTENT_IMAGE_ID | Image_Content_txt | Content_txt | Hashtags>**
    
    총 데이터 : 32,099
    
    동일 게시글 병합 : 25,196

* **ig_query_parser.py**
 : URL 상에서 유저의 아이디를 뽑아내는 소스코드
* **json_image_crawler.py**
 : json의 url을 통해 인스타 게시글 이미지를 다운로드 받는 소스코드
* **googleapi.py**
 : OCR을 작동시키는 소스
* **_human_parsing**
 : 게시글을 분석하여 json 파일을 만드는 소스코드


###  데이터 전처리

### 모델 생성
* Modeling
    * RNN, Seq2Seq 자료조사
    * GPT-2를 이용한 생성 모델 학습 진행 중
* 데이터 변형 
    * Translation (한글 →  다른 나라 언어 →  한글)
        * Google Translation API 이용
        
            |코드|설명|
            |:--------:|:--------:|
            |translateAPU.py|입력된 글을 영어로 번역한 뒤 한국어로 다시 번역해주는 코드|


* 명사 유의어로 변경하기 
    * Word2Vec

        |코드|설명|
        |:--------:|:--------:|
        |change_synonym.py|설명|
        |word2vec_train_and_save.py|설명|

word2vec_train_and_save.py


## 참고 문헌

## 참고 문헌
* NLP:
    * BERT 세미나 자료: <https://www.slideshare.net/WonIkCho/1909-bert-whyandhow-code-seminar>
    * 딥 러닝을 이용한 자연어 처리 입문: <https://wikidocs.net/book/2155>
    * 쉽게 씌어진 Word2Vec: <https://dreamgonfly.github.io/machine/learning,/natural/language/processing/2017/08/16/word2vec_explained.html>


* 데이터 수집:
    * instagram-crawler: <https://github.com/huaying/instagram-crawler>
    * Vision API Tutorial: <https://www.evernote.com/l/AZQhDK3EG1dPlYYGM7nz--qf_IpgswSIbQw/>

* 데이터 전처리
    * han-spell: <https://github.com/ssut/py-hanspell/blob/master/README.md>


* 모델링
    * gpt-2: <https://github.com/nshepperd/gpt-2>
    * gpt-2 colab: <https://colab.research.google.com/github/ilopezfr/gpt-2/blob/master/gpt-2-playground_.ipynb?fbclid=IwAR21GZFZ2gWHFwZmWss5osQpxDRuZOQsx_RXdvSbBWbyTYBogYru9bRB6qY#scrollTo=_QIdaQn5WkSf>
