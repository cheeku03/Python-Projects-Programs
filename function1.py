def scholarship(d):
        if 1<=d<=30:
            return 0
        elif 31<=d<=50:
            return 20
        elif 51<=d<=80:
           return 30
        elif 81<=d<100:
           return 50

def sch():
        x = float(input("Enter 10 percentage: "))
        y = float(input("Enter 12 percentage: "))
        m=max(x,y)
        if 0 <= m <= 50:
            return 0
        elif 50 <= m <= 100:
            return 50

c=(input("Have you given entrance exam?(yes or no)"))
if c=="yes":
    d=float(input("Enter Entrance Exam percentage:"))
    s=scholarship(d)

    t=sch()
    q = float(input("Enter your fees: "))
    p=max(s,t)
    print(p,"scholarship",p*q/100)


else:
   t=sch()
   q = float(input("Enter your fees: "))
   print(t,"scholarship",t*q/100)