class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return self.name + ' ' + self.sex + ' ' + str(self.age)
    def changename(self,name):
        self.name = name
    def changeage(self):
        self.age = self.age + 1
person1 = Person('Joe','F','40') #we create objects(person1 and person2) here for class Person
person2 = Person('John','M','32')
print('Person1:'+ str(person1))
person1.changeage()
print('Person1:'+ str(person1))