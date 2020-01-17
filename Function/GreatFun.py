
def great(num1,num2):
    if(num1>num2):
        return 0

    elif(num1<num2):
        return 1

    else:
        return 2


num1=int(input("enter first number"))
num2=int(input("enter second number"))

val=great(num1,num2)

if(val==0):
    print(num1, "is greater than", num2)
elif(val==1):
    print(num2, "is greater than", num1)
else:
    print(num1, "is equal to", num2)
