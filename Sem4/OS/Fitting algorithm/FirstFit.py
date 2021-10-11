import sys
def printf(format, *args):
    sys.stdout.write(format % args)

class FirstFit:
    def __init__(self):
        return None 

    def firstFit(self,block,process):

        m,n = len(block),len(process)

        allocation = [-1 for x in range(n)]

        for x in range(0,n):
            for y in range(0,m):
                if block[y] >= process[x]:
                    allocation[x] = y
                    block[y] -=process[x] 
                    break
            
                
        
        printf("\nProcess no. \t\t Process size \t\t Block No.\n")

        for x in range(0,n):
            if allocation[x] == -1:
                printf("%5d \t\t %15d \t\t Not Allocated\n",(x+1),process[x])
            else:
                printf("%5d \t\t %15d \t\t %5d\n",(x+1),process[x],(1+allocation[x]))
        return None



if __name__=="__main__":
    print("55_Adnan_Shaikh")
    block = [100,500,200,300,600]
    process = [500,90,112,426]
    firstf = FirstFit()
    firstf.firstFit(block,process)