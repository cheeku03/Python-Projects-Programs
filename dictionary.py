'''dict1={'one':'Jan','two':'Feb','three':'Mar','four':'April'}
x=dict1.popitem()
print(x)
print(len(dict1))
dict1.update({'five':'May','six':'june'})
print(len(dict1))
print(dict1)
for x in dict1:
    print(x, sep=',',end=' ')
   print()
for x in dict1:
print(dict1[x],sep=',',end=' ')
'''
'''for x in dict1.values():
    print(x, end=' ')
    print()
for x in dict1.keys():
    print(x, end=' ')
    print()
for x,y in dict1.items():
    print(x,y)'''

'''matrix=[[0,0,0,1,0],[2,0,0,0,3],[0,0,0,4,0]]
mat={(0,3):1, (1,0):2}
print(mat)
print(mat.get((0,1),0))'''

'''m={}
for x in "Mississippi":
    m[x]=m.get(x,0) +1
    print(m)'''

'''lst=[1,2,3,4,5]
lst2=lst
print(lst2)
lst[2]=10
print(lst)
'''

'''opposites={'up':'down','right':'wrong','true':'false'}
alias = opposites
print(alias is opposites)

alias['right']='left'
print(opposites['right'])'''