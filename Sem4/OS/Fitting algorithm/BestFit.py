import sys
def printf(format, *args):
    sys.stdout.write(format % args)

class BestFit:
    def __init__(self):
        return None 

    def bestFit(self,block,process):

        m,n = len(block),len(process)

        allocation = [-1 for x in range(n)]

        for x in range(0,n):
            best_index = -1
            for y in range(0,m):
                if block[y] >= process[x]:
                    if best_index == -1:
                        best_index = y
                    else:
                        if block[y]<block[best_index]:
                            best_index = y
            
            if best_index != -1:
                allocation[x] = best_index
                block[best_index] -=process[x]
        
        printf("\nProcess no. \t\t Process size \t\t Block No. \n")

        for x in range(0,n):
            if allocation[x] == -1:
                printf("%10d \t\t %10d \t\t Not Allocated\n",(x+1),process[x])
            else:
                printf("%5d \t\t %15d \t\t %8d\n",(x+1),process[x],(1+allocation[x]))
        return None



if __name__=="__main__":
    print("55_Adnan_Shaikh")
    block = [100,500,200,300,600]
    process = [212,417,112,426]
    bestf = BestFit()
    bestf.bestFit(block,process)

