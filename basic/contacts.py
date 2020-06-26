class Model:
    def __init__(self):
        self._name = ''
        self._phone = ''
        self._email = ''
        self._addr = ''

    @property
    def name(self) -> str: return self._name

    @name.setter
    def name(self, name): self._name = name

    @property
    def phone(self) -> str: return self._phone

    @phone.setter
    def phone(self, phone): self._phone = phone

    @property
    def email(self) -> str: return self._email

    @email.setter
    def email(self, email): self._email = email

    @property
    def addr(self) -> str: return self._addr

    @addr.setter
    def addr(self, addr): self._addr = addr

    def __str__(self) -> str:
        return self._name + ', ' + self._phone + ', ' + self._email + ', ' + self._addr

    def to_string(self) -> str:
        return 'name : {}, phone : {}, email : {}, addr : {}' \
            .format(self._name, self._phone, self._email, self._addr)




class Service:  # 객체만 둔다
    def __init__(self):
        self._contacts = []

    def add_contact(self, payload):
        self._contacts.append(payload)

    def get_contact(self, payload) -> object:
        for i in self._contacts:
            if payload == i.name:
                return i

    def get_contacts(self) -> []:
        contacts = []
        for i in self._contacts:
            contacts.append(i.to_string())
        return ' '.join(contacts)

    def del_contact(self, payload):
        for i, t in enumerate(self._contacts):  # i : index  t: elements
            if payload == t.name:
                del self._contacts[i]









class Controller:
    def __init__(self):
        self._service = Service()

    def register(self, name, phone, email, addr):
        model = Model()
        model.name = name #setter
        model.phone = phone
        model.email = email
        model.addr = addr
        self._service.add_contact(model)

    def search(self, payload) -> object:
        return self._service.get_contact(payload)

    def list(self):
        return self._service.get_contacts()

    def remove(self, payload):
        self._service.del_contact(payload)













def print_menu():
    print('0. Exit')
    print('1. add')
    print('2. name search')
    print('3. find all')
    print('4. name delete')
    return input('Menu\n')

app = Controller()
while 1:
    menu = print_menu()
    if menu == '1':
        app.register(input('name\n'),
                    input('phone\n'),
                    input('email\n'),
                    input('address\n'))

    if menu == '2':
        print(app.search(input('name\n')))

    if menu == '3':
        print(app.list())

    if menu == '4':
        app.remove(input('name\n'))

    elif menu == '0':
        break


