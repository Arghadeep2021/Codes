class student:
    #field name - grades(list), id, name
    grades=[]
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def addgrades(self,grade):
        self.grades.append(grade)
    def showgrades(self):
        grds = ' '
        for grade in self.grades:
            grds += str(grade) + ' '
        return grds
stu1 = student('John', '1234')
stu1.addgrades(90)
stu1.addgrades(88)
stu1.addgrades(86)
print(stu1.showgrades())
