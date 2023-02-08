package exp_1.program;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class ClientJava {
    public static void main(String[] args) throws IOException{
        String hostname = args[0];
        Integer portnumber = Integer.parseInt(args[1]);

        try(
            Socket sock = new Socket(hostname,portnumber);
            BufferedReader in = new BufferedReader(
                new InputStreamReader(
                    sock.getInputStream()
                )
            );
            PrintWriter out = new PrintWriter(sock.getOutputStream(),true);
        ){
            String fromServer, fromUser;
            Scanner stdIn = new Scanner(System.in);
            while((fromServer = in.readLine()) != null){
                
                System.out.println(fromServer);
                if (fromServer.equals("Bye.")) break;

                fromUser = stdIn.nextLine();
                if (fromUser!=null){
                    out.println(fromUser);
                }
            }
        }

    }
}
