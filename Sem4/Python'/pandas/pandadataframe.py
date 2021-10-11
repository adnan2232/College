import pandas as pd
key_lst = []
n = int(input("Enter number of elements : "))
num=int(input("\nSelect the type of input: \n1. Numerical \n2. String "))
if num == 1:
    for i in range(0, n):
        element1 = int(input("enter keys:"))
        key_lst.append(element1)
elif num == 2:
    for i in range(0, n):
        element1 = (input("enter keys:"))
        key_lst.append(element1)
value_lst = []
for i in range(0, n):
    value = (input("enter values: ")) 
    value_lst.append(value)
