def fibo(n):
    if(n==2):
        return 1
    elif(n==1):
        return 0
    else:
        return (fibo(n-1)+fibo(n-2))
print(fibo(5))

# fibo 4 = fibo 3 + fibo 2
# fibo 3 = fibo 2 + fibo 1