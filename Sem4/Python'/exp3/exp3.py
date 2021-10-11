def even_odd(l = []):
    even, odd = [], []
    for x in l:
        if x%2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even,odd

def merge_sort(l1 = [],l2 = []):
    lis = [*l1,*l2]
    return sorted(lis)

def update_delete(l = []):
    l[0] = input("Enter First value to update: ")
    del l[len(l)//2]
    return l

def minmax(l = []):
    return min(l),max(l)

def searching(l = []):
    num = input("Do you want to add element Y/N:").strip()
    if num.lower() == "y":
        l.append(input("Enter the element you want to append: "))
        searching(l)
    elif num.lower() == "n":
        if "python" in l:
            print("python is present in the list at position: ",l.index("python"))
        elif "Python" in l:
            print("python is present in the list at position: ",l.index("Python"))
        else:
            print("Python is not present in the list")
    else:
        print("You pressed wrong key please try again")
        searching(l)

if __name__ == "__main__":

    while(1):
        num = int(input("*********Menu Driven***************\n1. Separate Even and odd elements\n2. Merge and sort two lists \n3. Updating first element and deleting middle element\n4. Minimum and maximum value of a list\n5. Add names into list and check for python\n6. Exit\n"))
        if num == 1:
            l = list(map(int,input("Enter the element of the list: ").strip().split()))
            l1,l2 = even_odd(l)
            print(f"Even list: {l1}\nOdd list: {l2}")
        elif num == 2:
            l1 = list(map(int,input("Enter the element of first list: ").strip().split()))
            l2 = list(map(int,input("Enter the element of second list: ").strip().split()))
            l = merge_sort(l1,l2)
            print("Merged and sorted list: {}".format(l))
        elif num == 3:
            l = list(map(str,input("Enter the element of the list: ").strip().split()))
            l = update_delete(l)
            print(f"Modified list = {l}")
        elif num == 4:
            l = list(map(int,input("Enter the element of the list: ").strip().split()))
            mini, maxi = minmax(l)
            print(f"Maximum element of the list: {maxi}\nMinimum element of the list:{mini}")
        elif num == 5:
            searching([])
        elif num == 6:
            break
        else:
            print("you pressed wrong key please try again")
