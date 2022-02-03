```python
import pandas as pd

def multiplicative_inverse(a,n):
    r1,r2,t1,t2 = a,n,0,1
    arrays = [[] for _ in range(7)]
    
    while(r2>0):
        q = r1//r2
        arrays[0].append(q), arrays[1].append(r1), arrays[2].append(r2)
        
        r = r1 - q*r2
        r1,r2 = r2,r
        arrays[3].append(r), arrays[4].append(t1), arrays[5].append(t2)
        
        t = t1 - q*t2
        t1,t2 = t2,t
        arrays[6].append(t)
        
    b_inverse = t1 if r1 == 1 else False
    
    arrays[0].append(None), arrays[1].append(r1), arrays[2].append(r2)
    arrays[3].append(None), arrays[4].append(t1), arrays[5].append(t2)
    arrays[6].append(None)
    
    table = pd.DataFrame({
        "q": arrays[0],
        "r1": arrays[1],
        "r2": arrays[2],
        "r": arrays[3],
        "t1": arrays[4],
        "t2": arrays[5],
        "t": arrays[6]
    })
    
    return b_inverse,table    

a,n = map(int,input("Please enter the value of two numbers to find their multiplicative inverse: ").strip().split(" "))

b_inverse,table = multiplicative_inverse(a,n)

if not b_inverse:
    print("Inverse doesn't exist")
else:
    print(f"Inverse of b = {b_inverse+n if b_inverse<0 else b_inverse}")

table
```


```python

```
