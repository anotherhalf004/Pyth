import os
print(os.getcwd())
os.chdir("./newfolder")
print(os.getcwd())

folder = os.listdir()
t=j=p=1

for file in folder:
    if(file.endswith(".txt")):
        os.rename(f"./{file}",f'./{t}.txt')
        t+=1
    elif(file.endswith(".png")):
        os.rename(f"./{file}",f'./{p}.png')
        p+=1
    elif(file.endswith(".jpg")):
        os.rename(f"./{file}",f'./{j}.jpg')
        j+=1
    else:
        pass