import java.util.Scanner;



public class Exp_6{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int z;
        do{
            System.out.println("Enter : 1) for matrix addition  2) for String Operations 3) To exit ");
            z = sc.nextInt();
            switch(z){
                case 1: Matrix m = new Matrix();
                        m.op();
                        break;
                case 2: St s = new St();
                        s.op();
                        break;
                case 3: break;
                default : System.out.println("You Entered Wrong key please try again"); 
            }
        }while(z!=3);
    }
}

class Matrix{
    void op(){
        Scanner sc = new Scanner(System.in);
        int[][] arr_1 = new int[3][3];
        int[][] arr_2 = new int[3][3];

        System.out.println("Enter your first 3x3 Matrix \n");
        for(int i=0; i<3;i++){
            for(int j=0;j<3;j++){
                arr_1[i][j] = sc.nextInt();
            }
        }
        System.out.println("Enter your second 3x3 Matrix \n");
        for(int i=0; i<3;i++){
            for(int j=0;j<3;j++){
                arr_2[i][j] = sc.nextInt();
            }
        }
        System.out.println("Your Matrix addition: ");
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                System.out.print(arr_1[i][j]+arr_2[i][j]+"\t");
            }
            System.out.println();
        }
    }
}

class St{
    void op(){
        Scanner sc = new Scanner(System.in);
        String s = "";
        System.out.println("Checking if string is empty or not ");
        if(s.isEmpty())
            System.out.println("String is empty");
        else
            System.out.println("String is  not empty");
        System.out.print("Enter your String: ");
        s = sc.nextLine();
        System.out.println("\n your  String: "+s);
        System.out.println("Checking again if string is empty or not ");
        if(s.isEmpty())
            System.out.println("String is empty");
        else
            System.out.println("String is  not empty");
       for(int i=0;i<s.length();i++)
            System.out.println("Character at "+i+" Position is :"+s.charAt(i));
        String b;
        System.out.print("Enter string you want to concat :");
        b = sc.nextLine();
        System.out.println("Your concatinated string is :"+ s.concat(b));

        
    }
}