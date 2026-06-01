class Employee:
    companyName = "Apple"  # CLASS VARIABLE - shared with all 
    noofEmployees = 0      # class var usage as no . of emp for a company

    def __init__(self,name):
        self.name = name   
        self.raise_amount = 0.2 
        Employee.noofEmployees += 1 # CLASS VARIABLE ''(ClassName.var_name)'' - example to show usage of CLASS VARIABLE 
    def showDetails(self):
        print(f'Name of employee is {self.name} in {self.companyName} sized {self.noofEmployees} and raise amount of {self.raise_amount}')

# Employee.showDetails(e1)

e1 = Employee("Sasuke")
e1.companyName = "Apple India" # instance var here for e1 
e1.raise_amount = 0.3   # e1 instance variable - directly accesssed 
e1.showDetails()

print(Employee.companyName)
Employee.companyName = "Google"
print(Employee.companyName)


e2 = Employee("Naruto")
e2.companyName = "AWS"  # takes the instace var which is present instead  of class var 'Google'
e2.showDetails()

# first search for instance variablee for the current instance -, if not then uses class variable  