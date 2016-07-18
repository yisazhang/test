class dog:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self):
        return self.name + 'is eating'
d = dog ('wangcai', 'male', 3)
print d.eat()
      
