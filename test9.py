class people:
    def __init__(self, name, sex, age):
       self.name = name
       self.sex = sex
       self.age = age
class student(people):
    def __init__(self, name, sex, age, number):
       people. __init__(self, name, sex, age)
       self.number = number
    def learn(self):
       return self.name + 'is learning'
s = student('guanguan', 'male', 18, 10010)
print s.learn()
