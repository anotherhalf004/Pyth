qns = [
    ['What is best lang' , 'java', 'php' , 'python', 3],
    ['What is worst lang' , 'java', 'php' , 'python', 2],
    ['where sun rises' , 'east', 'west' , 'north', 1]
]

price=[
    1000,2000,5000,10000,12000,15000
]

total=0
i=0
for qn in qns:
    print(f'{qn[0]} .The options are 1.{qn[1]} 2.{qn[2]} 3.{qn[3]}')
    x=int(input('Enter option number: '))
    
    if(x==qn[4]):
        print("Thats correct!")
        total = total + price[i]
        i=i+1
    else:
        print('Game ki samapti!!!')
        print(f"The total is {total} rupees")
        break



