import java.util.*;
public class Exp_8 {
    public static void main(String[] args) {
        SingleH s = new SingleH();
        s.display();
        MultipleH m = new MultipleH();
        m.display();
        SuperClass h = new HierarchicalH();
        h.display();
    }
}
class SuperClass{
    void display(){
        System.out.println("Super class");
    }
}
class SingleH extends SuperClass{
    @Override
    void display(){
    System.out.println("You're in SingleH class");   
    System.out.println("Calling super class in subclass");
    super.display();
    }
    }

class MultipleH extends SingleH{
    @Override
    void display(){
        System.out.println("You're in MultipleH class");
        System.out.println("calling previous super class which will call root class");
        super.display();
    }
}
class HierarchicalH extends SuperClass{
    void display(){
        System.out.println("You're in HierarchicalH class which extends SuperClass (SuperClass is extended by 2 class viz SingleH and HierarchicalH which is an example of Hierarchical inheritance  )");
        System.out.println("Calling super class ");
        super.display();
    }
}