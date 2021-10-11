
#A accept 2 input string form user
def intake():
    str1 =input("Enter first string: ")
    str2 =input("Enter second string: ")
    print("first string is {} and second string is {}".format(str1, str2))
    print(str1, str2)

#B print common letter from input string(set insertion)
def com():
    str1 =input("Enter first string: ")
    str2 =input("Enter second string: ")
    setA=set(str1)
    setB=set(str2)
    common=list(setA&setB)
    print("Common letters in both the set is: ")
    for element in common:
        print(element)

#C Display letters which are in the first string but not in the second(set difference)
def diff():
    str1 =input("Enter first string: ")
    str2 =input("Enter second string: ")
    setA = set(str1)
    setB = set(str2)
    difference=list(setA-setB)
    print("Elements which are in A but not in B :")
    for element in difference:
        print(element)

#D Display set of common letters in both the strings (set union)
def un():
    str1 =input("Enter first string: ")
    str2 =input("Enter second string: ")
    setA = set(str1)
    setB = set(str2)
    union=list(setA|setB)
    print("Elements in both the sets: ")
    for element in union:
        print(element)

#E Displays letters which are in the two strings but not in both(symmetric difference)
def uncommon():
    str1 =input("Enter first string: ")
    str2 =input("Enter second string: ")
    setA = set(str1)
    setB = set(str2)
    uncommon=list(setA^setB)
    print("Element present in the strings but not in both the string: ")
    for element in uncommon:
        print(element)
if __name__=="__main__":

    while True:
        num = int(input("*********Menu Driven***************\n1. TO input strings \n2.To check common letters between two strings  \n3. To check letters which are in the first string but not in the second.\n4. To check set of common letters in both the strings  \n5. To check letters which are in the both the  strings but not in both \n6. Exit\n"))
        if num == 1:
            intake()
        elif num == 2:
            com()
        elif num == 3:
            diff()
        elif num ==4:
            un()
        elif num==5:
            uncommon()
        elif num==6:
            break

        else:
            print("Wrong key")


