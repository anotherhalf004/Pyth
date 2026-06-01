from math import sqrt as sq

class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j =j 
        self.k=k

    def __str__(self):
        return f'{self.i}i + {self.j}j + {self.k}k'
    
    def __add__(self, other):
        # return f'{self.i+other.i}i + {self.j+other.j}j + {self.k+other.k}k' ## Returns a  string but we need vector
        return Vector(self.i+other.i , self.j+other.j , self.k+other.k)
    
    def __gt__(self, other):  #  comparing Magnitude - √(a2+b2+c2)
        return sq( (self.i*self.i) + (self.j*self.j) + (self.k*self.k) ) > sq( (other.i*other.i) + (other.j*other.j) + (other.k*other.k) )
    
v1 = Vector(8,2,3)
v2 =Vector(3,4,5)
print(v1," ",v2)
print(v1+v2)
print(type(v1+v2))
print(v1>v2)

