def scan():
    thm = 0
    req = int(input("Enter the Number of Requests : "))
    hp = int(input("Enter the Initial Head Position : "))
    pos = hp
    srate = int(input("Enter the Seek Rate : "))
    print("Enter the Requests : ")
    arr = [ int(input()) for i in range(req)]
    start = 0
    end = int(input("Enter ending position of disk: "))
    print(hp, end='')
    if(hp<100):
        for i in range(pos, start-1, -1): 
            if i in arr:
                thm+= abs(pos-i)
                pos = i
                print(" -> ",i, end='')
                arr.remove(i)
        thm+= abs(pos-start)
        pos = start 
        print(" -> ", start, end='')
        for i in range(pos, end+1): 
            if i in arr:
                thm+= abs(pos-i)
                pos = i
                print(" -> ", i, end='')
                arr.remove(i)
    else:
        for i in range(pos, end+1):
            if i in arr:
                thm+= abs(pos-i)
                pos = i
                print(" -> ",i, end='')
                arr.remove(i)
        thm+= abs(pos-end)
        pos = end 
        print(" -> ", end, end='')
        for i in range(pos, start-1,-1): 
            if i in arr:
                thm+= abs(pos-i)
                pos = i
                print(" -> ", i, end='')
                arr.remove(i)
    stime = thm * srate
    print("\nThe Total Head Movement is",thm)
    print("The Seek Time is",stime)

if __name__ == "__main__":
    print("55_Adnan Shaikh")
    scan()