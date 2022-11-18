import numpy as np
from scipy.sparse import csr_matrix

r=int(input("Enter no. of rows: "))
c=int(input("Enter no. of columns: "))

l=[[int(input(f"Enter element of row {i+1} ,column {j+1}:")) for j in range(c)] for i in range(r)]
print("Dense matrix is:")
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print()
sp=csr_matrix(l)
print("\nSparse martrix:\n",sp)

