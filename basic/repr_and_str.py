class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'the repr: %s(%s)' % (self.name, self.age)

    def __str__(self):
        return 'the str: The person is %s, age is %s' % (self.name, self.age)


if __name__ == '__main__':
    tom = Person('tom', 18)
    print(tom)
    print(repr(tom))

