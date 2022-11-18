def fact(a):
    """recurive function to find out factorial"""
    if a==1:
        return 1
    else:
        return a*fact(a-1)
a=int(input("Enter a number: "))
print("Factorial of",a,"is",fact(a))