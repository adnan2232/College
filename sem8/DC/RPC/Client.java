import java.io.*;
import java.net.*;

class Client {
    public static void main(String[] args) throws Exception {
        Socket sock = new Socket("127.0.0.1", 3000);
        BufferedReader keyRead = new BufferedReader(new InputStreamReader(System.in));
        OutputStream ostream = sock.getOutputStream();
        PrintWriter pwrite = new PrintWriter(ostream, true);
        InputStream istream = sock.getInputStream();
        BufferedReader receiveRead = new BufferedReader(new InputStreamReader(istream));
        System.out.println("Client ready, type and press Enter key");
        String receiveMessage, sendMessage, temp;
        while (true) {
            System.out.println("\nEnter operation to perform(add,sub,mul,div and exit)....");
            temp = keyRead.readLine();
            sendMessage = temp.toLowerCase();
            if (!sendMessage.matches("add|sub|mul|div|exit")) {
                System.out.println("No operation name: " + sendMessage + "\nPlease try again");
                continue;
            }
            pwrite.println(sendMessage);
            if (sendMessage.equals("exit"))
                break;
            System.out.println("Enter first parameter :");
            sendMessage = keyRead.readLine();
            pwrite.println(sendMessage);
            System.out.println("Enter second parameter : ");
            sendMessage = keyRead.readLine();
            pwrite.println(sendMessage);
            System.out.flush();
            if ((receiveMessage = receiveRead.readLine()) != null)
                System.out.println(receiveMessage);
        }
        System.out.println("BYE");
    }
}