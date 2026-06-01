class Emp:
    def __init__(self,name):
        self.name = name
    # name = "Sunny"
    def __len__(self):
        i=0
        for l in self.name:
            i+=1 
        return i
    
    def __str__(self):                    
        return (f'Name({self.name})')
    
    def __repr__(self):                  ## if __str__ not present , fallback to __repr__
        return (f'Name({self.name}) repr')

    def __call__(self, *args, **kwds):
        print("Calling a object itself haha!")

