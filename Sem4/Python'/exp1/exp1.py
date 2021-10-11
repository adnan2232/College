num1, num2 = map(int,input("Enter Your Numbers: ").strip().split())

print(f'Bepfore Swapping: {num1}, {num2}')

num1, num2 = num2, num1

print(f'After Swapping: {num1}, {num2}')

num1, num2 = num2, num1

if num1 > 0:
    print("First number is positive!!!")
elif num1 < 0:
    print("First number is negative!!!")
else:
    print("First number is zero!!!") 