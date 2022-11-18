m=[]
r=int(input("Enter no. of row:"))
c=int(input("Enter no. of column:"))
for i in range(r):
    z=[]
    for j in range(c):
        a=int(input("Enter element "+str(i+1)+" row "+str(j+1)+" column: "))
        z+=[a]
    m.append(z)

n=[]
for i in range(c):
    q=[]
    for i in range(r):
                   q+=[0]
    n.append(q)
    
for i in range(r):
    for j in range(c):
        n[j][i]=m[i][j]
        
print("Transpose of Given Matrix is:")
for i in range(len(n)):
    print(i+1,"row is",n[i])
