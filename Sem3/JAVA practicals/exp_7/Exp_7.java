import java.util.Scanner;
import java.util.Vector;

public class Exp_7 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int z;
        do{
            System.out.println("Enter : 1) for String Buffer  2) for Vectors 3) To exit ");
            z = sc.nextInt();
            switch(z){
                case 1: SB s = new SB();
                        s.op();
                        break;
                case 2: VC v = new VC();
                        v.op();
                        break;
                case 3: break;
                default : System.out.println("You Entered Wrong key please try again"); 
            }
        }while(z!=3);
    }
}

class SB{
    void op(){
        StringBuffer sb = new StringBuffer("study");
		System.out.println("Before appending: "+sb);
		sb.append("tonight");
        System.out.println("After Appending: "+sb);
        System.out.println("Now passing int variable to append");
        StringBuffer str = new StringBuffer("test");
        System.out.println("Before appending: "+str);
        str.append(123);
		System.out.println("After  Appending:"+str);
        System.out.println("Inserting variable in between the string: ");
        str.insert(4, "code");
        System.out.println("After  inserting in middle:"+str);
        System.out.println("Reversing the string ");
        str.reverse();
        System.out.println("After reversing: "+str);
        StringBuffer st = new StringBuffer("Hello Jason");
        System.out.println("Replacing Substring from the string: ");
        System.out.println("Before replacing: "+st);
        st.replace(6, 11, "Java");
        System.out.println("After replacing: "+st);
        System.out.println("Initial Capacity: "+st.capacity()); 
		st.ensureCapacity(30); 
		System.out.println( "After Increasing the capacity: "+st.capacity());
    }
}

class VC{
    void op(){
        Vector<String> vec = new Vector<String>(4);  
           
          vec.add("Tiger");  
          vec.add("Lion");  
          vec.add("Dog");  
          vec.add("Elephant");  
          
          System.out.println("Size is: "+vec.size());  
          System.out.println("Default capacity is: "+vec.capacity());  
            
          System.out.println("Vector element is: "+vec);  
          vec.addElement("Rat");  
          vec.addElement("Cat");  
          vec.addElement("Deer");  
            
          System.out.println("Size after addition: "+vec.size());  
          System.out.println("Capacity after addition is: "+vec.capacity());  
           
          System.out.println("Elements are: "+vec);  
                   
            if(vec.contains("Tiger"))  
            {  
               System.out.println("Tiger is present at the index " +vec.indexOf("Tiger"));  
            }  
            else  
            {  
               System.out.println("Tiger is not present in the list.");  
            }  
              
          System.out.println("The first animal of the vector is = "+vec.firstElement());   
           
          System.out.println("The last animal of the vector is = "+vec.lastElement());  
    }
}