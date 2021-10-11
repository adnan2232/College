

public class FF{
    public static void firstfit(int[] block,int[] process,int m,int n){
        int[] allocation = new int[n];
        for(int i=0;i<n;i++){
            allocation[i] = -1;
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(block[j]>=process[i]){
                    allocation[i] = j;
                    block[j] -= process[i];
                    break;
                }
            }
        }

        System.out.println("\nProcess no. \t\t Process size \t\t Block No.");

        for(int i=0; i<n; i++){
            if(allocation[i]==-1){
                System.out.printf("%10d \t\t %10d \t\t Not Allocated\n",(i+1),process[i]);
            }else{
                System.out.printf("%5d \t\t %15d \t\t %8d\n",(i+1),process[i],(1+allocation[i]));
            }
        }
    }
    public static void main(String[] args) {
        int[] block = {100,500,200,300,600};
        int[] process = {500,90,112,426};
        int m = block.length;
        int n = process.length;
        firstfit(block,process,m,n);
    }
}


        
