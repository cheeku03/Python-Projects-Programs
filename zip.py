s=[1,2,3,4,5]
s2=[4,5,6,7,8,9]
q=[]
for i in s:
    if i in s2:
        q.append(i)
print(q)
