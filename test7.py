class Student:
    def __init__(self,name,sex,age,number):
        self.name = name
        self.sex = sex
        self.age = age
        self.number = number

    def learn(self):
        return self.name +  'is learning'
s=Student('guanguan','male',18,10000100)
print s.learn()
