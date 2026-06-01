x =[1,2,3]
print(dir(x))
print(x.__add__)

## __dict__ --> Returns a dictionary representation of obj's attributes
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p =Person("Sunny", 20)
print(p.__dict__)
