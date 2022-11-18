def error_handling():
    """This function is for handling the value error """
    c=0
    while c==0:
        try:    #this block is trying to executes the statement, if comes error it goes to except block
            r=float(input("Enter: "))
            c=1
            return r
        except ValueError:
             """ this block is used to handle different types of error  , instead of giving error
             the statements in this block will be executed """
             print("\n\tInvalid! Only Enter Numbers\n")
             c=0

def details(t1,t2,t3,t4,t5):
    """this function is asking the user to enter the details"""

    s = input("Enter Your name: ")
    r = (input("Enter your roll no.: "))
    print("Marks in Paper 1")
    m1 = error_handling() #calling this function to check whether marks given is alphabets or integer
    print("Marks in Paper 2")
    m2 = error_handling() #here we again doing the same
    score = m1 + m2
    t1 += (s,)
    t2 += (r,)
    t3 += (m1,)
    t4 += (m2,)
    t5 += (score,)
    print("Details Added Successfully")
    return t1, t2, t3, t4, t5 #returing all values becoz to access these values outside this function

def update(t1, t2, t3, t4, t5):
    """this function is updating the details provided by the user"""

    print("\tA.Name")
    print("\tB.Roll no.")
    print("\tC.Marks")
    ch = (input("What you want to update? "))
    if ch == "A":
        l = list(t1)
        r=(input("What's the roll no of the NAME you want to update: "))
        if r in t2:
            a = t2.index(r)
            s = input("\t\tEnter Updated Name:")
            l[a] = s
            t1 = tuple(l)
        else:
            print("Enter Valid Roll no.")
    elif ch=="B":
        l = list(t2)
        r = input("What's the Name of the Student ? ")
        if r in t1:
            a = t1.index(r)
            s = (input("\t\tEnter Updated Roll no.:"))
            l[a] = s
            t2 = tuple(l)
        else:
            print("Invalid Name")
    elif ch=="C":
        l1, l2, l3 = list(t3), list(t4), list(t5)
        r = (input("What's the roll no of the student?"))
        if r in t2:
            a = t2.index(r)
            print("\tUpdated Paper 1 Marks")
            s = error_handling() #here we again checking marks, if it is alphabet or string
            print("\tUpdated Paper 2 Marks")
            s1 = error_handling() #again checking marks,if it is alphabet or string
            l1[a] = s
            l2[a] = s1
            l3[a] = s + s1
            t5 = tuple(l3)
            t3, t4 = tuple(l1), tuple(l2)
        else:
            print("Invalid roll no")
    else:
        print("Invalid Input")
    print("Updated Details are:")
    print(f"\nName:{t1}\nRoll no:{t2}\nPaper 1 Marks:{t3}\nPaper 2 Marks:{t4}\nTotal Score:{t5}")
    return t1,t2,t3,t4,t5 #returning updated values , to access them outside
t1=t2=t3=t4=t5=tuple()
while True: #condition is True becoz we don't know how many details , user will enter.
    print("\n\tMENU")
    print("1.Enter details.")
    print("2.Update Details")
    print("3.Exit")
    ch = int(input("Enter your Choice: "))
    if ch == 1 :
        t1, t2, t3, t4, t5 = details(t1, t2, t3, t4, t5)
    elif ch == 2 :
        t1,t2,t3,t4,t5=update(t1,t2,t3,t4,t5)
    elif ch==3:
        print("Details are:")
        print(f"\nName:{t1}\nRoll no: {t2}\nPaper 1 Marks: {t3}\nPaper 2 Marks: {t4}\nTotal Score: {t5}")
        break
    else:
        print("Enter Correct Choice")
