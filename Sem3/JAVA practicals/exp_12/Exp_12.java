

public class Exp_12 {
    public static void main(String[] args) {  
    try  
        {  
        int arr[]= {15,53,25,78};  
        System.out.println(arr[8]);    
        }  
             
        catch(ArrayIndexOutOfBoundsException e)  
        {  
            System.out.println(e);  
        }  
        try  
        {  
        int data=50/0;   
  
        }  
             
        catch(ArithmeticException e)  
        {  
            System.out.println(e);  
        }  

        finally{
            System.out.println("End of the program");
        }
    }  
}
