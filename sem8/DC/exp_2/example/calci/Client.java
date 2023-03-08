package calci;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Arrays;
import java.util.Scanner;


public class Client {
    
    private Client(){}
    public static void main(String[] args) {
        String host = (args.length>0) ? args[0]:null;
        Scanner sc = new Scanner(System.in);
        try{
            Registry registry = LocateRegistry.getRegistry(host);
            calci_interface stub = (calci_interface) registry.lookup("Calci");
            
            while(true){
                System.out.println("1. Add\n2.Multiply\n3. Exit");
                String key = sc.nextLine().toLowerCase();
                if(key.equals("exit")) break;
                switch(key){
                    case "add":
                        System.out.print("Enter your numbers: ");
                        System.out.println("result: "+stub.addNum(
                            Arrays.stream(
                                sc.nextLine().split("\\s+")
                            ).mapToInt(Integer::parseInt).toArray()
                        ));
                        break;

                    case "multiply":
                        System.out.print("Enter your numbers: ");
                        System.out.println("result: "+stub.multiply(
                            Arrays.stream(
                                sc.nextLine().split("\\s+")
                            ).mapToDouble(Double::parseDouble).toArray()
                        ));
                        break;

                    default:
                        System.out.println("Command: "+key+" not found");
                        break;

                }
                
            }
        }
        catch (Exception e){
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }

}
