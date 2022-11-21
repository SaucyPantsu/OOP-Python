class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print('My name is', self.name)
        city = 'Dublin'

    def print_city(self, city):
        print('My name is', self.name, ' and I live in', city)


Ryan = Person('Ryan')
Ryan.print_name()
Ryan.print_city()
print(Ryan.city)
print(Ryan.name)
