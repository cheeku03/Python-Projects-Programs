
b=0
a=" "
while a!="":
    a=(input("Enter no to add: "))
    if a!="":
        b+=float(a)
        a=(input("enter another no"))
    else:
        print("Sum is :",b)
        break
a=0
while a<=10:
    if a%2==0:
        if a==6:
            break
        print(a)
    a+=1

