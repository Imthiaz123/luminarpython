#properties to check

lst=[]                   #define
print(type(lst))

lst=[10,20,30]  #same type of data
print(lst)

lst=[10,10.5,"abc"] #diff type of data possible
print(lst)

lst=[10,20,20]      #duplicates possible
print(lst)

lst=[10,20,30.5]    #mutable (can update values)
lst[0]=100
print(lst)

lst=[10,"abc",20]   #o/p oreder is same as input order.Insertion order preserved
print(lst)

lst.append(250)         #to append data at end...lst=[250] will overwrite
print(lst)

lst.insert(0,250)   #will append data at particular index
print(lst)

lst=[10,20,30,4]        #get value at particular index
print(lst[0])


#iterate through list and print list method 1
lst=[10,20,3,4]
cnt=len(lst)
print(cnt)
for i in range(0,cnt):
    print("list:",lst[i])

#other method to iterate through list method 2
for item in lst:                #values in lst stored to item and print it
    print(item)



#to get user input
lst=list()
limit=int(input("enter limit of list:"))
for i in range(0,limit):
    val=int(input("enter value:"))
    lst.append(val)
print(lst)





