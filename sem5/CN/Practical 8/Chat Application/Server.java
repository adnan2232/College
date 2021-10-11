package chatapp;
import java.util.*;
import java.io.*;
import java.net.*;


public class Server{
    static HashMap<Integer,ClientHandler> acc = new HashMap<Integer,ClientHandler>();
    static int count = 0;
    public static void main(String args[]) throws IOException {
        
        ServerSocket ss = new ServerSocket(200);
        
        while(true){
            Socket s = ss.accept();
            ClientHandler ct = new ClientHandler("client "+count, new DataInputStream(s.getInputStream()), new DataOutputStream(s.getOutputStream()),s);
            Thread t = new Thread(ct);
            acc.put(count, ct);
            count++;
            t.start();
        }
    }

}

class ClientHandler implements Runnable{
    private final String name;
    final DataInputStream dis;
    final DataOutputStream dos;
    public final Socket s; 
    boolean loggedin;
    public ClientHandler(String name,DataInputStream dis,DataOutputStream dos,Socket s){
        this.name = name;
        this.dis = dis;
        this.dos = dos;
        this.s = s;
        this.loggedin = true;
    }
    @Override
    public void run(){
        while(true){
            String receive;
            try{
                receive = this.dis.readUTF();
                if(receive.equals("logout")){
                    this.loggedin = false;
                    this.s.close();
                    break;
                }
                if(receive.contains("#")){
                    StringTokenizer st = new StringTokenizer(receive,"#");
                    String msg = st.nextToken();
                    String name = st.nextToken();
                    ClientHandler cc = Server.acc.get(Character.getNumericValue(name.charAt(name.length()-1)));
                    if(cc == null || !cc.loggedin){
                        this.dos.writeUTF("Client not found");
                    }
                    
                    else{
                        cc.dos.writeUTF(this.name+": "+msg);
                    }
                }
                else{
                    this.dos.writeUTF("Wrong Input");
                }
            }catch (IOException e){
                e.printStackTrace();
            }
        }
    }
}