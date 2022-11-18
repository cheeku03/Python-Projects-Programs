r=int(input("Enter no. of rows: "))
c=int(input("Enter no. of columns: "))
k=[]

for i in range(r):
    k2 = []
    for j in range(c):
        print(f"Enter element of row {i+1} ,column {j+1}:",end=" ")
        e=int(input())
        k2.append(e)
    k.append(k2)
print("\nMatrix is:")
for i in k:
    print(i)

# l=[[int(input(f"Enter element of row {i+1} ,column {j+1}:")) for j in range(c)] for i in range(r)]
# print("\nMatrix is:")
# for i in l:
#     print(i)
