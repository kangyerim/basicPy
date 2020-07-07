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
        self.noun_tokens = []
        self.okt = Okt()
        self.stopword = [] #소음
        self.freqtxt = []

    def extract_texts(self, payload): #페이로드 => 엔티티(파이썬) = 모델(자바)
        print('111 >> text문서에서 token 추출')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.texts = f.read()
        print(f'111 결과물 >> {self.texts[:300]}')


    def tokenize(self):
        print('222 >> corpus 에서 korean 추출')
        texts = self.texts.replace('\n','')
        tokenizer = re.compile(r'[^ㄱ-힣]')
        # ^는 not과 start 두가지 개념이 있음
        # [^]는 not, ^[]은 start 의미로 표현됨
        self.texts = tokenizer.sub(' ', texts)
        # 한글이 아닌 것은 ''처리해서 한글과 띄어쓰기까지 남겨라
        print(f'222 결과물 >> {self.texts[:300]}')

    def conversion_token(self):
        print('333 >> corpus 에서 korean 추출')
        self.tokens = word_tokenize(self.texts)
        print(f'333 결과물 >> {self.tokens[:300]}')

    def compound_noun(self):
        print('444 >> korean token 변환')
        _arr = []
        for token in self.tokens:
            token_pos = self.okt.pos(token)
            _ = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
            if len("".join(_)) > 1:
                _arr.append("".join(_))
        self.noun_tokens = " ".join(_arr)
        print(f'444 결과물 >> {self.noun_tokens[:300]}')

    def extract_stopword(self, payload):
        print('555 >> 복합명사화')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.stopword = f.read()
        print(f'555 >> 복합명사화 >> {self.stopword[:300]}')

    def filtering_text_with_stopword(self):
        print('666 >> 노이즈 필터링 후 시그널 추출')
        self.noun_tokens = word_tokenize(self.noun_tokens)
        self.noun_tokens = [text for text in self.noun_tokens
                            if text not in self.stopword]

    def frequent_text(self):
        print('777 >> 시그널 중에 사용빈도 정렬')
        self.freqtxt = pd.Series(dict(FreqDist(self.noun_tokens))).sort_values(ascending=False)
        print(f'{self.freqtxt[:10]}')

    def wordcloud(self, payload):
        print('8. 시각화')
        fname = payload.context + payload.fname
        wcloud = WordCloud(fname, relative_scaling=0.2, background_color='white') \
            .generate(" ".join(self.noun_tokens))
        plt.figure(figsize=(12, 12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

class Controller:
    def __init__(self):
        pass

    def download_dictionary(self):
        nltk.download('all')

    def data_analysis(self):
        entity = Entity()
        service = Service()
        entity.context = './data' #setContext
        entity.fname = '/kr-Report_2018.txt' #setFname : 위에서 _줘서 먹는 것
        service.extract_texts(entity)
        service.tokenize() # 한글에서 추가
        service.conversion_token() # 한글에서 추가
        service.compound_noun() # 명사 조합
        entity.fname = '/stopwords.txt'
        service.extract_stopword(entity) # 소음 처리
        service.filtering_text_with_stopword() # stopword 걸러내기
        service.frequent_text() #빈도수로 텍스트 정렬
        entity.fname = '/D2Coding.ttf'
        service.wordcloud(entity)

def print_menu():
    print('0.exit\n')
    print('1. dictonary download\n')
    print('2. data analysis\n')
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
