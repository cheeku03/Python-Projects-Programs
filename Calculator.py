#Calculator
print("CALCULATOR")
a=float(input("Enter first number: "))
b=float(input("Enter second Number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. FloorDivision")
c=int(input("Enter your choice(1...5):"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
elif c==5:
    print(a//b)
else:
    print("Invalid Input")