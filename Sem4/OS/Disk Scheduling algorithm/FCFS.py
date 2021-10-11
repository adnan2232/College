def fcfs():
    thm = 0
    req = int(input("Enter the Number of Requests : "))
    hp = int(input("Enter the Initial Head Position : "))
    srate = int(input("Enter the Seek Rate : "))
    print("Enter the Requests : ")
    arr = [ int(input()) for i in range(req)]
    thm = thm + abs(hp - arr[0])
    print(str(hp)+" -> "+str(arr[0]), end='')
    for i in range(1, req): 
        thm = thm + abs(arr[i] - arr[i-1])
        print(" -> "+str(arr[i]), end='')
    stime = srate * thm
    print("\nThe Total Head Movement is",thm)
    print("The Seek Time is",stime)


if __name__ == "__main__":
    print("55_Adnan Shaikh")
    fcfs()