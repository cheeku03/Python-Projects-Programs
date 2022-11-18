#interest calculator
p=float(input("enter principal amount: "))
r=float(input("enter rate (annum in %): "))
t=float(input("Enter time(months): "))
t=t/12
SI=(p*r*t)/100
#print("Simple Interest is :",SI)
n=int(input("How many times interest will applied in year? "))
amount=p*((1+(r)/n)**(n*t))
print(amount)
CI=amount-p
print("Compound Interest is :",CI)