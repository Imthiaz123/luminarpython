def secGreat(num1,num2,num3):
    if(((num1>num2)&(num1<num3)|((num1<num2)&(num1>num3)))):
        return 0
    elif(((num2>num1)&(num2<num3)|((num2<num1)&(num2>num3)))):
        return 1
    elif(((num3>num1)&(num3<num2)|((num3<num1)&(num3>num2)))):
        return 2
    else:
        return 3

num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))

res=secGreat(num1,num2,num3)

if(res==0):
    print(num1, "is second largest")
elif(res==1):
    print(num2, "is second largest")
elif(res==2):
    print(num3, "is second largest")
else:
    print("numbers are equal")


