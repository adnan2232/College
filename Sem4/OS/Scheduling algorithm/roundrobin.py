from prettytable import PrettyTable

def rr():
    pid,at,bt,tt,wt = [],[],[],[],[]
    print()
    z = int(input("Enter number of Process: "))
    ct = [0]*z
    quantum = int(input("Enter the quantum time: "))
    print()
    
    for i in range(0,z):
        pid.append(int(input("Enter Proccess id:")))
        print()
        at.append(int(input("Enter arrival time:")))
        print() 
        bt.append(int(input("Enter burst time:")))
        print()
        
    for i in range(0,z):
        min = [pid[i],at[i],bt[i]]    
        j = i-1
        while(j>=0 and at[j]>min[1]):
            at[j+1],pid[j+1],bt[j+1] = at[j],pid[j],bt[j]
            j = j-1
        pid[j+1],at[j+1],bt[j+1] = min[0],min[1],min[2]

    rem_bt = bt.copy()
    tot = 0
    while(True):
        status = True

        for x in range(0,z):
            if rem_bt[x] > 0:
                status = False

                if (rem_bt[x]-quantum)>0:
                    rem_bt[x] -= quantum
                    tot += quantum
                else:
                    tot += rem_bt[x]
                    ct[x] = tot+1
                    rem_bt[x] = 0
        if status:
            break

    tt.append(ct[0]-at[0])
    wt.append(tt[0]-bt[0])


    for i in range(1,z):
        
        tt.append(ct[i]-at[i])
        wt.append(tt[i]-bt[i]) 

    
    x = PrettyTable()
    x.field_names = ["Process id","Arrival Time","Burst Time","Completion Time","Turnaround Time","Waiting Time"]

    for a,b,c,d,e,f in zip(pid,at,bt,ct,tt,wt):
        x.add_row([a,b,c,d,e,f])
    
    print(x)

    print("Total turnaround time: "+str(sum(tt))+"\nTotal waiting time: "+str(sum(wt)))   
    print("Average turnaround time: "+str(sum(tt)/z)+"\nAverage waiting time: "+str(sum(wt)/z))   



    
    

      


if __name__ == "__main__":
    print("55_Adnan_Shaikh")
    rr()