class Stack:
    def __init__(self):
        self.stack = []

    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        if len(self.stack) > 0:
            print(self.stack.pop())
        else:
            print("Stack is empty!!!")
    
    def display(self):
        print(self.stack)

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,val):
        self.queue.append(val)

    def dequeue(self):
        if len(self.queue) > 0:
            print(self.queue.pop(0))
        else:
            print("Queue is empty!!!")
    
    def display(self):
        print(self.queue)