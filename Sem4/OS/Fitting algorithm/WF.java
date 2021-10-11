public class WF{
    public static void worstFit(int[] block,int[] process,int m,int n){
        int[] allocation = new int[n];
        int worst_indx;
        for(int i=0;i<n;i++){
            allocation[i] = -1;
        }

        for(int i=0;i<n;i++){
            worst_indx = -1;
            for(int j=0;j<m;j++){
                if(block[j]>=process[i]){
                    if(worst_indx == -1)
                        worst_indx = j;
                    else{
                        if(block[j]>block[worst_indx])
                            worst_indx = j;
                    }
                }
            }
            if(worst_indx!=-1){
                allocation[i] = worst_indx;
                block[worst_indx] -= process[i];
            }
        }

        System.out.println("\nProcess no. \t\t Process size \t\t Block No.");

        for(int i=0; i<n; i++){
            if(allocation[i]==-1){
                System.out.printf("%5d \t\t %15d \t\t Not Allocated\n",(i+1),process[i]);
            }else{
                System.out.printf("%5d \t\t %15d \t\t %8d\n",(i+1),process[i],(1+allocation[i]));
            }
        }
    }

    public static void main(String[] args) {
        int[] block = {100,500,200,300};
        int[] process = {500,400,600,426};
        int m = block.length;
        int n = process.length;
        worstFit(block,process,m,n);
    }
}
