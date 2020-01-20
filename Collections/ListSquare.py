lst = list()
evenlst=list()
oddlst=list()
sum = 0
limit = int(input("enter limit of list:"))

for i in range(0, limit):
    val = int(input("enter value:"))
    lst.append(val)
    if(val%2==0):
        evenlst.append(lst[i])
    else:
        oddlst.append(lst[i])
leng=len(evenlst)

print("List:",lst)
print("Even numbers:",evenlst)
print("odd numbers:",oddlst)

for j in range(0,leng):
        evenlst[j]=evenlst[j]**2
        sum=sum+evenlst[j]

print("Even Number Square:",evenlst)
print("sum:",sum)


