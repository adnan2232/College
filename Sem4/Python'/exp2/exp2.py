def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

def palindrome(str):
    if str == str[::-1]:
        print(f"{str} is palindrome!!!")
    else:
        print(f"{str} is not a palindrome!!!")

if __name__ == "__main__":

    while(1):
        num = int(input("*********Menu Driven***************\n1. To calculate factorial\n2. To check given number or string is palindrome!!!!\n3. Exit\n"))
        if num == 1:
            n = int(input("Enter your number: "))
            z = factorial(n)
            print(f"{n}! = {z}")
        elif num == 2:
            palindrome(input("Enter number or a string: "))
        elif num == 3:
            break
        else:
            print("you pressed wrong key please try again")


