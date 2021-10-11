class FIFO:
    def __init__(self,p,fs):
        self.p = p
        self.fs = fs
        self.n = len(self.p)

    def search(self,key,f):
        for i in range(self.fs):
            if f[i] == key:
                return True
        return False


    def fifo(self):
        f = [-1 for i in range(self.fs)] 
        hit = 0
        k = 0
        for i in range(self.n):
            if(self.search(self.p[i],f)):
                hit += 1
                print(str(self.p[i])+"\t\t  No")
                continue
            if k<self.fs:
                f[k] = self.p[i]
                k += 1
                
            if k == self.fs:
                k =0
            print(str(self.p[i])+"\t"+str(f[0])+" "+str(f[1])+" "+str(f[2])+"\t  Yes")

        print("Number of hits = "+str(hit))
        print("Number of miss = "+str(self.n-hit))
            



if __name__ == '__main__':
    print("55_Adnan Shaikh")
    x = input("Enter elements of reference string use comma: ")
    p = [int(i.replace(" ","")) for i in x.split(',')]
    fs= int(input("Enter the frame size: "))

    fif = FIFO(p,fs)
    print("PAGE\tFRAME\tPAGE FAULT")
    fif.fifo()

