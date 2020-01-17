
def greater(num1,num2,num3):
    if((num1>num2)&(num1>num3)):
        return 0

    elif((num2>num1)&(num2>num3)):
        return 1

    else:
        return 2


num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))

res=greater(num1,num2,num3)

if(res==0):
    print(num1, "is greater")
elif(res==1):
    print(num2, "is greater")
else:
    print(num3, "is greater")
