public class CandO {
 
  static int x = 1;
  public CandO(){
  System.out.println("Object "+x+" is created");
  x++;
  }

  public static void main(String[] args) {
    CandO myObj1 = new CandO();  // Object 1
    CandO myObj2 = new CandO();  // Object 2
  }
}