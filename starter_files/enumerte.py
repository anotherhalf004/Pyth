# marks=[23,234,121,41,4,11]

# for index,mark in enumerate(marks):
#     print(mark)
#     if(index==3):
#         print("This is 3th index")

#returns a tuple containing index and value of each element in sequence
# default starts from index 0

marks=[23,234,121,41,4,11]

for index,mark in enumerate(marks,start=2):
    print(mark)
    if(index==3):
        print(index)
        print("This is 3th index")



