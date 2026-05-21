a=[1,2,3]
b=[1,2,3]
#F,T

a=2
b=2
#T,T a is b - True ?? => 2 is constant num ( IMMUTABLE) , value not gonna change thus no need to create new mem thus a is b
 
A=(1,3)
B=(1,3)
#T,T 

print(a is b) # exact location of object in memory

print(a==b)  #value