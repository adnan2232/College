package calci;
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface calci_interface extends Remote{
    int addNum(int... arr) throws RemoteException;
 
    double multiply(double... arr) throws RemoteException;
}
