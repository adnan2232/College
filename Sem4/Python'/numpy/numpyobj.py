import numpy as np

x = int(input("enter number of rows: "))
y = int(input("enter number of columns: ")) 

matrix = lambda : [list(map(int,input().strip().split())) for _ in range(x)]
for i in range(2):
    print("matrix: ", i + 1)
    if i==0:
        mat1=np.array(matrix())
    elif i==1:
        mat2=np.array(matrix())

print("matrix 1 is: ")
print(mat1)
print("matrix 2 is: ")
print(mat2)
res = np.dot(mat1, mat2)

print("Multiplication of matrix 1 and 2 is : \n",res)
