import math
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

number_list = [6,-9,420.69,'banana']
 
for number in number_list:
    try:
        number_factorial = math.factorial(number)
    except TypeError:
        print("Factorial is not supported for given input type. \n")
    except ValueError:
        print(f"Factorial only accepts whole values. {number} is not a whole value. \n")
    else:
        print(f"The factorial of {number} is {number_factorial}\n")
    finally:
        print("Release any resources in use. \n")
