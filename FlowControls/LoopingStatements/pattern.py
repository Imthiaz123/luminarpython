#for i in range(0,3):
 #   for j in range(0,3):
  #      print(i,end="")
   # print()

#for i in range(0,3):
 #   for j in range(0,3):
  #      print(j,end="")
   # print()

num=int(input("enter number of rows"))
for i in range(0,num+1):
    for j in range(0,i):
        print("*",end=" ")
    print()

print("\n")
num=int(input("enter number of rows"))
for i in range(0,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


print("\n")
num=int(input("enter number of rows"))
for i in range(num,0,-1):
    for j in range(1,i+1):
            print(j,end=" ")

    print()
