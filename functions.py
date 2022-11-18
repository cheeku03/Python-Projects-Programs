def calc(a,b=2,c=3):
    print(a,b,c)
    print(a+b+c)
    print(a*b*c)
def name(a,b,c=12):
    print("name=",a,"age=",b,"class=",c)

def mul(*args):
    p=1
    for i in args:
        p*=i
    return p
a=mul(3,2,5,6)

def pair(**kwargs):
    for a,b in kwargs.items():
        print(a,b)

pair( hi = "hello" , mid = "hii",chirag="guys")