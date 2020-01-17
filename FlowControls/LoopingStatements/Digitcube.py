num=int(input("enter number:"))

rev=0
while(num!=0):
    rem=num%10
    rev=rev+(rem**3)
    num=num//10
print(rev)