class InvalidProductException extends Exception
{
    public InvalidProductException(String s)
    {
        
        super(s);
    }
}
 
public class Exp_13
{
   void productCheck(int weight) throws InvalidProductException{
	if(weight<100){
		throw new InvalidProductException("Product Invalid");
	}
   }
   
    public static void main(String args[])
    {
    	Exp_13 obj = new Exp_13();
        try
        {
            obj.productCheck(60);
        }
        catch (InvalidProductException ex)
        {
            System.out.println("Caught the exception");
            System.out.println(ex.getMessage());
        }
    }
}
