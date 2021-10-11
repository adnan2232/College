from prettytable import PrettyTable

def fcfs():
    pid,at,bt,ct,tt,wt = [],[],[],[],[],[]
    print()
    z = int(input("Enter number of Process: "))
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

    ct.append(at[0]+bt[0])
    tt.append(ct[0]-at[0])
    wt.append(tt[0]-bt[0])


    for i in range(1,z):
        ct.append(at[i]+bt[i]) if (at[i] > ct[i-1]) else  ct.append(ct[i-1]+bt[i])
        tt.append(ct[i]-at[i])
        wt.append(tt[i]-bt[i]) 

    for i in range(0,z):
        min = [pid[i],at[i],bt[i],ct[i],tt[i],wt[i]]    
        j = i-1
        while(j>=0 and pid[j]>min[0]):
            at[j+1],pid[j+1],bt[j+1],ct[j+1],tt[j+1],wt[j+1] = at[j],pid[j],bt[j],ct[j],tt[j],wt[j]
            j = j-1
        pid[j+1],at[j+1],bt[j+1],ct[j+1],tt[j+1],wt[j+1] = min[0],min[1],min[2],min[3],min[4],min[5]
    

    x = PrettyTable()
    x.field_names = ["Process id","Arrival Time","Burst Time","Completion Time","Turnaround Time","Waiting Time"]

    for a,b,c,d,e,f in zip(pid,at,bt,ct,tt,wt):
        x.add_row([a,b,c,d,e,f])
    
    print(x)

    print("Total turnaround time: "+str(sum(tt))+"\nTotal waiting time: "+str(sum(wt)))   
    print("Average turnaround time: "+str(sum(tt)/z)+"\nAverage waiting time: "+str(sum(wt)/z))   


if __name__ == "__main__":
    print("55_Adnan_Shaikh")
    fcfs()