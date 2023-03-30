
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;


public class Client {
    static long givenTime;
    public static void main(String[] args) throws IOException,ParseException{
        DateFormat sdf = new SimpleDateFormat("hh:mm:ss");
        givenTime = sdf.parse(args[0]).getTime() + (new Date()).getTime();
        
        System.out.println("Current Time: "+new Date(givenTime));
        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run(){
                givenTime += 100;
            }
        }, 0, 100);
        try(
            Socket sock = new Socket("localhost",6969);
            BufferedReader in = new BufferedReader(
                new InputStreamReader(
                    sock.getInputStream()
                )
            );
            PrintWriter out = new PrintWriter(sock.getOutputStream(),true);
        ){
            String fromServer;
        
            while((fromServer = in.readLine()) != null){
                
                if (fromServer.equals("send time")){
                    out.println(givenTime);
                    System.out.println("Send Time:"+new Date(givenTime));
                }else if(fromServer.chars().allMatch( Character::isDigit)|| (fromServer.startsWith("-") && fromServer.substring(1).chars().allMatch( Character::isDigit))){
                    givenTime = Long.parseLong(fromServer);
                    
                    System.out.println("New Date From Server: "+new Date(givenTime));
                }else if(fromServer.equals("exit")){
                    System.out.println("Server shutdown exiting: ");
                    break;
                }else{
                    System.out.println("From Server: "+fromServer);
                }
                
            }
        }
    }
}
