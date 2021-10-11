
public class Exp_11 {
    public static void main(String[] args) {
        SuperClass h = new SingleH();
        h.display();
        NoHerit n = new NoHerit();
        n.display();
    }
}

class SuperClass{
    void display(){
        System.out.println("Super class");
    }
}
class SingleH extends SuperClass{
    void display(){
    System.out.println("You're in SingleH class");   
    System.out.println("Calling super class in subclass");
    super.display();
    }
    }
final class NoHerit{
    void display(){
        System.out.println("This class is using final keyword it cannot be inerited further ");
    }
}