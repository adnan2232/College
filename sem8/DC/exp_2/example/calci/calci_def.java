package calci;

class Calci implements calci_interface{

    public Calci(){}

    public int addNum(int... arr){
        int total = 0;
        
        for(int x: arr) total += x;

        return total;
    }


    public double multiply(double... arr){
        double res = 1;
        for(double x:arr) res *= x;
        return res;
    }
}