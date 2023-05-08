class Person(object):
    total = 10
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

# class의 상속성을 이용! 계속해서 재사용하기 위해 class를 사용한다.

print(type(Person))
my = Person("Moon", 22)
print(my.name)
print(my.age)
print(my.getName())
print(my.getAge())
print(my.total)

you = Person("kim", 20)
print(you.getName())
print(you.getAge())
print(you.total)