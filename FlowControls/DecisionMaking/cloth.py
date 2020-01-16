type=int(input("1.Cotton\n2.Silk\n3.Linen\nselect type of cloth:"))
amount=int(input("Enter purchase amount:"))
if(type==1):
    print("cloth type:cotton")
    if(amount>20000):
        discount=amount*(10/100)
        amount1=amount-discount
    elif((amount>15000)&(amount<=20000)):
        discount=amount*(9/100)
        amount1 = amount - discount
    elif((amount>14000)&(amount<=15000)):
        discount=amount*(7/100)
        amount1 = amount - discount
    else:
        discount=amount*(2/100)
        amount1 = amount - discount
elif(type==2):
    print("cloth type:silk")
    if(amount>20000):
        discount=amount*(15/100)
        amount1 = amount - discount
    elif((amount>15000)&(amount<=20000)):
        discount=amount*(10/100)
        amount1 = amount - discount
    elif((amount>14000)&(amount<=15000)):
        discount=amount*(9/100)
        amount1 = amount - discount
    else:
        discount=amount*(5/100)
        amount1 = amount - discount
else:
    print("cloth type:linen")
    if(amount>20000):
        discount=amount*(15/100)
        amount1 = amount - discount
    elif((amount>15000)&(amount<=20000)):
        discount=amount*(10/100)
        amount1 = amount - discount
    elif((amount>14000)&(amount<=15000)):
        discount=amount*(9/100)
        amount1 = amount - discount
    else:
        discount=amount*(5/100)
        amount1 = amount - discount

print("Purchase Amount is Rs",amount)
print("Amount after offer is Rs",int(discount))
print("Final amount is Rs",int(amount1))
