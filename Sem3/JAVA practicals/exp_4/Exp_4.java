import java.util.Scanner;

public class Exp_4{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double l,b,s;
        System.out.print("Enter Rectangle length and breadth: ");
        l = sc.nextDouble();
        b = sc.nextDouble();
        System.out.print("\n Enter side  of square:  ");
        s = sc.nextDouble();
        System.out.println();
        Overload o1 = new Overload();
        Overload o2 = new Overload("Constructor overloaded successfully ");
        System.out.println("Area of square: "+ o1.Area(s)+"\n Area of recatangle: "+o1.Area(l,b));

    }
}


class Overload{
    public Overload(){
        System.out.println("Empty overloaded Constructor");
    }
    public Overload(String v){
        System.out.println("This overloaded constructor takes String \n your given string is "+v);
    }
    double Area(double l, double b){

        return l*b;
    }
    double Area(double s){
        return s*s;
    }
}