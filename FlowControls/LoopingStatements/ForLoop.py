#for i in range(0,10):
 #   print(i)

#for i in range(0,10,2):#2 is step (increment by 2)
 #   print("even:",i)

#for i in range(1,10,2):
 #   print("odd",i)

num1=int(input("enter lower limit"))
num2=int(input("enter upper limit"))
for i in range(num1,num2,2):
    print(i)

for i in range(0,10):
    if(i%2==0):
        print("even:",i)