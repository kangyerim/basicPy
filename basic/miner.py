from dataclasses import dataclass
import nltk
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
from nltk import FreqDist

import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

@dataclass
class Entity:
    context: str
    fname: str
    target: str


    @property
    def context(self) -> str: return self._context
    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def target(self) -> str: return self._target
    @target.setter
    def target(self, target): self._target = target


class Service:
    def __init__(self):
        self.texts = [] #신호 : 목적성에 맞으면 신호
        self.tokens = []
        self.okt = Okt()
        self.stopword = [] #소음
        self.freqtxt = []

    def extract_token(self, payload):
        print('111 >> text문서에서 token 추출')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.texts = f.read()
        print(f'111 결과물 >> {self.texts[:300]}')


    def extract_hanguel(self):
        print('222 >> corpus 에서 korean 추출')
        texts = self.texts.replace('\n','')
        tokenizer = re.compile(r'[^ㄱ-힣]')
        # ^는 not과 start 두가지 개념이 있음
        # [^]는 not, ^[]은 start 의미로 표현됨
        self.texts = tokenizer.sub('', texts)
        # 한글이 아닌 것은 ''처리해서 한글만 남겨라
        print(f'222 결과물 >> {self.texts[:300]}')

    def conversion_token(self):
        print('>> corpus 에서 korean 추출')
        pass

    def compound_noun(self):
        print('>> korean token 변환')
        pass

    def extract_stopword(self):
        print('>> 복합명사화')
        pass

    def filtering_text_with_stopword(self):
        print('>> 노이즈 필터링 후 시그널 추출')
        pass

    def frequent_text(self):
        print('>> 시그널 중에 사용빈도 정렬')
        pass

    def wordcloud(self):
        print('>> 시각화')
        pass


class Controller:
    def __init__(self):
        pass

    def download_dictionary(self):
        nltk.download('all')

    def data_analysis(self):
        entity = Entity()
        service = Service()
        service.extract_token()
        service.extract_hanguel() # 한글에서 추가
        service.conversion_token() # 한글에서 추가
        service.compound_noun() # 명사 조합
        service.extract_stopword() # 소음 처리
        service.filtering_text_with_stopword() # stopword 걸러내기
        service.frequent_text() #빈도수로 텍스트 정렬
        service.wordcloud()

def print_menu():
    print('0.exit\n')
    print('1. dictonary download\n')
    return input('menu \n')

app = Controller()
while 1:
    menu = print_menu()
    if menu == '1':
        app.download_dictionary()
    if menu == '2':
        app.data_analysis()
    elif menu == '0':
        break
