def rev(num):
    rev=0
    while(num!=0):
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    return rev

num=int(input("enter number:"))
res=rev(num)
print("reverse:",res)
