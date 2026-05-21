import random


def fn(x,a):
    if (x==a):
        print("Its a tie! try again ?")
    elif(x=="ROCK"):
        print(f"Computer chooses {x}")
        if(a==2):
            print("YOU WIN!")
        else:
            print("YOU LOSE")
    elif(x=="PAPER"):
        print(f"Computer chooses {x}")
        if(a==1):
            print("YOU LOSE")
        else:
            print("YOU WIN!")
    else:
        print(f"Computer chooses {x}")
        if(a==1):
            print('YOU WIN!')
        else:
            print("YOU LOSE")
for i in range(3):
    print("---ROCK PAPER SCISSORS---")
    a = int(input("1- ROCK , 2-PAPER , 3-SCISSORS\n"))

    l=["ROCK","PAPER","SCISSORS"]
    x = random.choice(l)
    fn(x,a)

# LENGTHY COMPLEX TO UNDERSTAND 













