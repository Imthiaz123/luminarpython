def fact(num):
    i=1
    fact=1
    while(i<=num):
        fact=fact*i
        i+=1
    return fact
num=int(input("enter number:"))
res=fact(num)
print("factorial:",res)