class Employee:
    company = "Apple"

    def show(self):
        print(f"Name is {self.name} and company is {self.company}")
    
    @classmethod
    def changeComp(cls,newComp):
        cls.company = newComp

    # def __init__(self,name,salary):
    #     self.name = name
    #     self.salary = salary

e1 = Employee()
e1.name = "Sunny"
e1.show()

e1.changeComp("Google")    # for instance ( when not used @classmethod )
e1.show()
print(Employee.company)
print("NEXT :\n")


######################--- AS ALTERNATIVE CONSTRUCTORS ---##########################

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def fromStr(cls,string):
        # return cls(string.split("-")[0],int(string.split("-")[1]))  # cls(... , ...) this passes to the class's constructor
        # # or this (￣┰￣*)
        name , age = string.split("-")
        return cls(name,int(age))
    
p1 = Person.fromStr("Sunny-12000")
print(p1.name)
print(p1.age)

        
        



