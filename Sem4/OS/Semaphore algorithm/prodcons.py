mutex,full,empty,x = 1,0,3,0

def wait(s):
    global mutex,full,empty,x
    s -=1
    return s

def signal(s):
    global mutex,full,empty,x
    s += 1
    return s



def producer():
    global mutex,full,empty,x
    mutex = wait(mutex)
    full = signal(full)
    empty = wait(empty)
    x +=1
    print("Producer produces the item: "+str(x))
    mutex = signal(mutex)

def consumer():
    global mutex,full,empty,x
    mutex = wait(mutex)
    full = wait(full)
    empty = signal(empty)
    print("Consumer consumes item: "+str(x))
    x -=1
    mutex = signal(mutex)

    

if __name__ == "__main__":
    print("55_Adnan Shaikh")
    print("1.Producer \n2.Consumer \n3.Exit")

    while(1):
        n = int(input("Enter your choice: "))

        if n == 1:
            if mutex == 1 and empty != 0:
                producer()
            else:
                print("Buffer is full")
        elif n == 2:
            if  mutex == 1 and full != 0:
                consumer()
            else:
                print("Buffer is empty!!")
        elif n == 3:
            break
        else:
            print("You pressed wrong key please try")

             