
num=int(input("enter number:"))
flag=0
for i in range(2,num):

    if(num%i==0):
        flag=flag+1
        break
    else:
        flag=0
if(flag==0):
    print("number is prime")
else:
    print("number is not prime")



num1=int(input("enter lower limit:"))
num2=int(input("enter upper limit:"))

for val in range(num1,num2):
    for i in range(2, val):
        if((val%i)==0):
            break
    else:
        print(val)



num1=int(input("enter lower limit:"))
num2=int(input("enter upper limit:"))
sum=0

for val in range(num1,num2):
    flag = 1
    for i in range(2, int(val/2)):
        if((val%i)==0):
            flag=0
            break
    if(flag==1):
        sum=sum+val

print("sum=",sum)



