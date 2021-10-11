from StackQueue.stack_queue import Stack,Queue

if __name__ == "__main__":
    
    while True:
        num = int(input("**************Menu Driven**************\n1.Implementing Stack\n2.Implementing Queue\n3.Exit\n"))
        if num == 1:
            s = Stack()
            while True:
                n = int(input("1.Push\n2.Pop\n3.Display\n4.Back\n"))
                if n == 1:
                    s.push(input("Enter element you want to push: "))
                elif n == 2:
                    s.pop()
                elif n == 3:
                    s.display()
                elif n == 4:
                    break
                else:
                    print("You pressed wrong key please try agin")
        elif num == 2:
            q = Queue()
            while True:
                n = int(input("1.Enqueue\n2.Dequeue\n3.Display\n4.Back\n"))
                if n == 1:
                    q.enqueue(input("Enter element you want to enqueue: "))
                elif n == 2:
                    q.dequeue()
                elif n == 3:
                    q.display()
                elif n == 4:
                    break
                else:
                    print("You pressed wrong key please try agin")
        elif num == 3:
            break
        else:
            print("You pressed wrong key please try again")



    