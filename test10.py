class animal:
    def __init__(self, name, sex, age):
       self.name = name
       self.sex = sex
       self.age = age
class dog(animal):
    def __init__(self, name, sex, age, number):
       animal.__init__(self, name, sex, age)
       self.number = number
    def eat(self):
       return s.name + 'is eating'
s = dog('wangcai', 'male', 8, 110)
print s.eat() 
