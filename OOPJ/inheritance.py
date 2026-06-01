class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f'Name of employee is {self.name} and id - {self.id}')

class Programmer(Employee):

    #USE OF super()
    def __init__(self, name):
        super().__init__(name)   # USING PARENT CLASS METHODS by ''super().''
        self. id = id
    
    def showLang(self):
        print('Default lang is python')

    #Method Overiding
    def showDetails(self):
        print(f'Name - {self.name} & id - {self.id}')



e = Employee("Andrez" , 3)
e.showDetails()

e1 = Programmer("Sunny", 1 )
e1.showDetails()
e1.showLang()