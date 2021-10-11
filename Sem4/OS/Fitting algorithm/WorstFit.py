import sys
def printf(format, *args):
    sys.stdout.write(format % args)

class WorstFit:
    def __init__(self):
        return None 

    def worstFit(self,block,process):

        m,n = len(block),len(process)

        allocation = [-1 for x in range(n)]

        for x in range(0,n):
            worst_index = -1
            for y in range(0,m):
                if block[y] >= process[x]:
                    if worst_index == -1:
                        worst_index = y
                    else:
                        if block[y]>block[worst_index]:
                            worst_index = y
            
            if worst_index != -1:
                allocation[x] = worst_index
                block[worst_index] -=process[x]
        
        printf("\nProcess no. \t\t Process size \t\t Block No.\n")

        for x in range(0,n):
            if allocation[x] == -1:
                printf("%5d \t\t %15d \t\t Not Allocated\n",(x+1),process[x])
            else:
                printf("%5d \t\t %15d \t\t %5d\n",(x+1),process[x],(1+allocation[x]))
        return None



if __name__=="__main__":
    print("55_Adnan_Shaikh")
    block = [100,500,200,300]
    process = [500,400,600,426]
    worstf = WorstFit()
    worstf.worstFit(block,process)
