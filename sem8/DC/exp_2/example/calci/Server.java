package calci;

import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;

public class Server {
    public Server(){}
    
    public static void main(String[] args) {
        try{
            calci_interface skeCalci = (calci_interface) UnicastRemoteObject.exportObject(
                new Calci(),0
            );

            Registry registry = LocateRegistry.getRegistry();
            registry.bind("Calci",skeCalci);

            System.out.println("Server is ready");
        }
        catch (Exception e){
            System.err.println("Server Exception: "+e.toString());
            e.printStackTrace();
        }
    }
}
