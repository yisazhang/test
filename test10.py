class Animal:
    def __init__(self, name, sex, age):
       self.name = name
       self.sex = sex
       self.age = age
class Dog(Animal):
    def __init__(self, name, sex, age, number):
       Animal.__init__(self, name, sex, age)
       self.number = number
    def eat(self):
       return s.name + 'is eating'
s = Dog('wangcai', 'male', 8, 110)
print s.eat() 
