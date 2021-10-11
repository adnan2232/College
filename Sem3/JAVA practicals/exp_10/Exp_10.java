

public class Exp_10 {
    public static void main(String[] args) {
        Student s = new Info("Jonathan Joester", 68, "11/B", 72323);
        s.display();
    }    
}

abstract class Student{
    private String name;
    private int roll_no;
    private String grade;
    public Student(String name,int roll_no,String grade){
        this.name = name;
        this.roll_no = roll_no;
        this.grade = grade;
    }
    public abstract void display();
    public void show(){
        System.out.println("Student name: "+this.name+"\n Roll no: "+this.roll_no+"\n Standard: "+this.grade);
    }

}

class Info extends Student{
       int gr_no;
        public Info(String name,int roll_no,String grade,int gr_no){
            super(name, roll_no,grade);
            this.gr_no = gr_no;
        }
        public void display(){
            System.out.println("Your entered information is : ");
            super.show();
            System.out.println("\n Student gr_no: "+this.gr_no);
        }
}