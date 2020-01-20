#print even numbers from list
lst=[10,20,25,22,18,33,4]
cnt=len(lst)
print(cnt)
print("even list:")
for i in range(0,cnt):
    if(lst[i]%2==0):
        print(lst[i])