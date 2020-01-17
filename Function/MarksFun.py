
def marks(num1,num2,num3):
    total=num1+num2+num3
    print("total=",total)
    if(total>145):
        return 0

    elif((total>140)&(total<=145)):
        return 1

    elif((total>135)&(total<=140)):
        return 2

    elif((total>130)&(total<=135)):
        return 3

    elif(total<= 30):
        return 4


num1=int(input("Enter mark of first subject"))
num2=int(input("Enter mark of second subject"))
num3=int(input("Enter mark of third subject"))

res=marks(num1,num2,num3)
if(res==0):
    print("grade is A+")
if(res==1):
    print("grade is A")
if(res==2):
    print("grade is B+")
if(res==3):
    print("grade is B")
if(res==4):
    print("failed")
















