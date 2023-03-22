import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;

class Server{
    public static void main(String[] args) {
        try(
            ServerSocket sock = new ServerSocket(6969);
            
        ){  

        }catch(Exception e){
            e.printStackTrace();
        }
    }
}


class ClientSockets{
    public static ArrayList<Socket> clientList = new ArrayList<>();
    private static  int count = 0;
    private static final String CLIENT="CLIENT_";
    Socket socket;
    String nameString;
    DataOutputStream sockDos;
    DataInputStream sockDis;

    ClientSockets(Socket socket) throws IOException{
        count++;
        this.socket = socket;
        this.nameString = CLIENT+count;
        this.sockDos = new DataOutputStream(this.socket.getOutputStream());
        this.sockDis = new DataInputStream(this.socket.getInputStream());
    }

}