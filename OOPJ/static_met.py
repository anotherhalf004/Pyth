class Math:
    def __init__(self,num):
        self.num = num
    def adddtonum(self,n):
        self.num = self.num + n
    
    @staticmethod  # no need to pass 'self'
    def add(a,b):
        return a+b
    
a = Math(9)
print(a.num)
a.adddtonum(2)
print(a.num)

# calling the static  method using class or the instance
print(Math.add(9,2))
# print(a.add(9,2))