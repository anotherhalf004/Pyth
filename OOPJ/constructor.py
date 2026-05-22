# class Person:
#     name ="sunny"
#     occ = "Student"

#     def __init__(self,name,o):
#         print("This is a person")   # Default Constructor - Doesnt accept any args from object and has only one (self) arg 
#         # print("Contructor runs automatically always when a object is created ")
#         self.name = name            # Parametrized
#         self.occ = o                # Constructor

#     def info(self):
#         print(f"{self.name} is a {self.occ}")


# a=Person("Jon","King in North") # self is automatically passed
# b=Person("Arya","Faceless Girl")
# a.info()
# b.info()


# PYTHON DECORATORS - Modify functions

def greet(fx):
    def modifiedfx(*args,**kwargs):
        print("Good morning")
        fx(*args,**kwargs)
        print("Thnk for using function")
    return modifiedfx

@greet
def hello():
    print("Hello World")

@greet
def add(x,y):
    print(x+y)


hello() 
# or greet(hello)() 
add(2,4)
# greet(add)(2,4)
#               OUTPUT                
# Good morning
# Hello World
# Thnk for using function
# Good morning
# 6
# Thnk for using function












