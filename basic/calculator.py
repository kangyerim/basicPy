class Model:
    def __init__(self):
        self._num1 = 0
        self._num2 = 0
        self._opcode = ''

    @property
    def num1(self) -> int: return self._num1
    @num1.setter
    def num1(self, num1): self._num1 = num1

    @property
    def num2(self) -> int: return self._num2
    @num2.setter
    def num2(self,num2): self._num2 = num2

    @property
    def opcode(self) -> str: return self._opcode
    @opcode.setter
    def opcode(self, opcode): self._opcode = opcode




class Service:
    def __init__(self, payload):   #self는 공간을 차지 않음/ 검은색만 자리차지
        self._num1 = payload.num1
        self._num2 = payload.num2

    def add(self):
        return self._num1 + self._num2

    def minus(self):
        return self._num1 - self._num2

    def multi(self):
        return self._num1 * self._num2

    def divide(self):
        return self._1 / self._num2








class Controller:
    def __init__(self): # 생성자에서 할 거 없으면 생략가능
        pass

    def calc(self, num1, num2, opcode):
        model = Model()    # new Model()
        model.num1 = num1  # setNum1
        model.num2 = num2
        model.opcode = opcode

        service = Service(model)
        if opcode == '+': result = service.add()
        if opcode == '-': result = service.minus()
        if opcode == '*': result = service.multi()
        if opcode == '/': result = service.divide()
        return result













def print_menu():
    print('0. Exit')
    print('1. Calculator')
    return input('Menu\n')

while 1:        # 이게 스위치케이스
    menu = print_menu()
    if menu == '0' :break
    if menu == '1' :
        app = Controller()
        print('계산기 작동')

        num1 = int(input('첫번째 수\n'))
        opcode = input('연산자\n')
        num2 = int(input('두번째수\n'))

        result = app.calc(num1, num2, opcode)
        print('결과 : %d' % result)