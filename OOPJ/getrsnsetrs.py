class Myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value is {self._value}")   

    @property                               #
    def get_tenx_value(self):                   # getter
        return 10*self._value               #
    
    @get_tenx_value.setter                      # setter
    def set_tenx_value(self,new_value):             
        self._value = new_value/10
    
obj = Myclass(10)
obj.set_tenx_value = 34
obj.show()
print(obj.get_tenx_value)


