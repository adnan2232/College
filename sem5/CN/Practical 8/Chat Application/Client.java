package chatapp;
import java.util.*;
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws IOException{
        InetAddress ip = InetAddress.getByName("localhost");
        Socket s= new Socket(ip,200);
        Thread sm = new Thread(new SendMessage(s, new DataOutputStream(s.getOutputStream())));
        Thread rm = new Thread(new ReadMessage(s, new DataInputStream(s.getInputStream())));
        sm.start();
        rm.start();
        
    }
}


class SendMessage implements Runnable{
    Scanner sc = new Scanner(System.in);
    final private Socket s;
    DataOutputStream dos;
    public SendMessage(Socket s, DataOutputStream dos){
        this.s = s;
        this.dos = dos;
    } 
    @Override
    public void run(){
        while(true){
            try{
                this.dos.writeUTF(sc.nextLine());
            }catch(IOException e){
                e.printStackTrace();
            }
        }
    }
}

class ReadMessage implements Runnable{
    final private Socket s;
    DataInputStream dis;
    public ReadMessage(Socket s, DataInputStream dis){
        this.s = s;
        this.dis = dis;
    } 
    @Override
    public void run(){
        while(true){
            try{
                System.out.println(this.dis.readUTF());
            }catch(IOException e){
                e.printStackTrace();
            }
        }
    }
}