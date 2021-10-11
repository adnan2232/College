#numberGuessing
class ValueTooSmallError(Exception):
    #Raised when the input value is too small
    pass
class ValueTooLargeError(Exception):
    #Raised when the input value is too large
    pass

number = 10
while True:
    try:
        i_num = int(input("Guess the number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")
