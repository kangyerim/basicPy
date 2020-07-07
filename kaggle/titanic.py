import pandas as pd

class Entity:
# context(str), fname(str), train(object), test(object), id(str),
# label(str) : ERD에서 결정되는 것들
    context: str  
    fname: str
    train: object
    test: object
    id: str
    label: str

    @property
    def context(self) -> str: return self._context
    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str : return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object : return self._train
    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object  : return self._test
    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str : return self._id
    @id.setter
    def id(self, id) :  self._id = id

    @property
    def label(self) -> str: return self._label
    @label.setter
    def label(self, label): self._label = label

"""
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
print(f’결정트리 활용한 검증 정확도 {None}‘)
print(f’랜덤포레스트 활용한 검증 정확도 {None}‘)
print(f’나이브베이즈 활용한 검증 정확도 {None}‘)
print(f’KNN 활용한 검증 정확도 {None}‘)
print(f’SVM 활용한 검증 정확도 {None}’)
"""
class Service:
    def __init__(self):
        self.entity = Entity() # autowired Entity

    def new_model(self, payload):
        this = self.entity
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)


class Controller:
    def __init__(self):
        self.entity = Entity()  # autowired
        self.service = Service()  # autowired

    def modeling(self, train, test): # csv파일을 넣는다
        service = self.service
        this = self.preprocess(train, test) # payload는 객체를 받을 때
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train)
        this.test =  service.new_model(test)
        #print(f'트레인 컬럼 : {this.train.columns}')
        print(f'테스트 컬럼 : {this.test.columns}')

def print_menu():
    print('0.Exit')
    print('1.Go')
    return input('Menu\n')

app = Controller()
while 1:
    menu = print_menu()
    if menu == '0' : break
    if menu == '1' :
        app.preprocess('train.csv', 'test.csv')
        break