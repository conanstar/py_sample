class Person(object):
    def __new__(cls, name, age):
        print('__new__ called.')
        return super().__new__(cls)

    def __init__(self, name, age):
        print('__init__ called.')
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)


class PositiveInteger(int):
    def __init__(self, value):
        super().__init__(self, abs(value))


if __name__ == '__main__':
    john = Person('john', 24)
    print(john)
