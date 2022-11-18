print("Enter 1 to enter a string")
print("Enter 2 for numbers")
ch=int(input("Enter your choice:"))
if ch==1:
    a=input("Enter a string:")
    b=input("Enter another string:")
    c=a+b
    print(c,isinstance(c,str))
elif ch==2:
    a=float(input("Enter fist no. :"))
    b=float(input("enter second no. :"))
    print("Enter 1 for /")
    print("Enter 2 for //")
    print("Enter 3 for %")
    ch1=int(input("enter your choice:"))
    if ch1==1:
        d=a/b
        print(d,isinstance(d,float))
    elif ch==2:
        f=a//b
        print(f,isinstance(f,int))
    elif ch==3:
        m=a%b
        print(m,isinstance(m,float))
    else:
        print("invalid input")
else:
    print("Invaid input")


# a=eval(input())
# print(type(a))