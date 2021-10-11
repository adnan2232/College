
# Create key/value pair dictionary
#global dictionary
my_dict={1: "java", 2: "c", 3: "python"}


#update dictionary
def update():
    key=int(input("enter the key to be updated: "))
    value=input("Enter value: ")
    my_dict[key]=value
    print("updated dictionary: ",my_dict)

#concatenate dictionary
def concatenate():
    key_lst = []
    value_lst = []
    n = int(input("Enter number of pairs: "))
    # iterating till the range
    for i in range(0, n):
        keys = int(input("enter key: "))
        key_lst.append(keys)
        value = (input("enter value: "))
        value_lst.append(value)

    my_dict_2= dict(zip(key_lst, value_lst))
    my_dict.update(my_dict_2)
    print("after concatenation:= ", my_dict)
    return my_dict

def delete():
    #delete value from dicitonary
    key=int(input("enter the key to be deleted:="))
    del my_dict[key]
    print("Dictionary after deleting key {} associated with its value is:= {}".format(key, my_dict))

def find():
    #find a key and print its value
    key_list=list(my_dict.keys())
    value_list=list(my_dict.values())
    print("keys from dictionary my_dict",key_list)
    x=int(input("Enter the key to be viewed:="))
    value=key_list.index(x)
    print("associated value to the selected key {} is : {}".format(x, value_list[value]))
def combine_linst():
    key_lst = []
    n = int(input("Enter number of elements : "))
    # iterating till the range
    for i in range(0, n):
        element1 = int(input("enter key list:"))
        key_lst.append(element1)
    value_lst = []
    # iterating till the range
    for i in range(0, n):
        value= (input("enter value list: "))
        value_lst.append(value)
    #map two lists into dictionary
    combined_list=dict(zip(key_lst, value_lst))
    print("after combining two list of keys(key_list) and values(value_list)", combined_list)


if __name__=="__main__":
    print(my_dict)
    while True:
        num = int(input("*********Menu Driven***************\n1. TO update dicitonary \n2.To concatenate dicitionary  \n3. To delete values from dictionary.\n4. To find value from dictionary \n5. To create dictionary from lists. \n6. Exit\n"))
        if num == 1:
            update()
        elif num == 2:
            concatenate()
        elif num == 3:
            delete()
        elif num ==4:
            find()
        elif num==5:
           combine_linst()
        elif num==6:
            break
        else:
            print("Wrong key")

