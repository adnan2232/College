import numpy as np

#array method x = [2, 3, 4, 5, 6]
nums = np.array([2, 3, 4, 5, 6]) 
print(type(nums))

#arrange method 
nums=np.arange(2,10)
print(nums)

#zero method 
nums=np.zeros((5,4)) 
print(nums)

#ones method 
nums=np.ones((5,4)) 
print(nums)

#linespace methods
nums=np.linspace(1,10,5) 
print(nums)

#eye method 
nums=np.eye(4) 
print(nums)

#random method

nums = np.random.rand(2,3) 
print(nums)

#reshaping array 
num=np.arange(1,17) 
num2=num.reshape(4,4) 
print(num2)

#findind max,min value 
random=np.random.randint(1,100,5) 
print(random)
xmin=random.min() 
print(xmin)

xmax=random.max() 
print(xmax)
