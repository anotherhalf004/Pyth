class Person:
    name = "sunny"
    age = 19
    occupation = 'student' 
    def info(self):         # SELF ka  mtlb voh object jispe method call ho rha hai
        print(f"{self.name} is a {self.occupation}")  

a = Person()
b=Person()

b.name = "Ned Stark"
b.occupation = "King in North"
b.info()

# a.name = "Denia"
# a.occupation = "cute wife"
# print(a.name, a.occupation)
a.info()














