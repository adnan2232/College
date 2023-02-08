package exp_1.program;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

class ServerJava{


    public static class KnockKnockProtocol {
        private static final int WAITING = 0;
        private static final int SENTKNOCKKNOCK = 1;
        private static final int SENTCLUE = 2;
        private static final int ANOTHER = 3;
    
        private static final int NUMJOKES = 5;
    
        private int state = WAITING;
        private int currentJoke = 0;
    
        private String[] clues = { "Turnip", "Little Old Lady", "Atch", "Who", "Who" };
        private String[] answers = { "Turnip the heat, it's cold in here!",
                                     "I didn't know you could yodel!",
                                     "Bless you!",
                                     "Is there an owl in here?",
                                     "Is there an echo in here?" };
    
        public String processInput(String theInput) {
            String theOutput = null;
    
            if (state == WAITING) {
                theOutput = "Knock! Knock!";
                state = SENTKNOCKKNOCK;
            } else if (state == SENTKNOCKKNOCK) {
                if (theInput.equalsIgnoreCase("Who's there?")) {
                    theOutput = clues[currentJoke];
                    state = SENTCLUE;
                } else {
                    theOutput = "You're supposed to say \"Who's there?\"! " +
                    "Try again. Knock! Knock!";
                }
            } else if (state == SENTCLUE) {
                if (theInput.equalsIgnoreCase(clues[currentJoke] + " who?")) {
                    theOutput = answers[currentJoke] + " Want another? (y/n)";
                    state = ANOTHER;
                } else {
                    theOutput = "You're supposed to say \"" + 
                    clues[currentJoke] + 
                    " who?\"" + 
                    "! Try again. Knock! Knock!";
                    state = SENTKNOCKKNOCK;
                }
            } else if (state == ANOTHER) {
                if (theInput.equalsIgnoreCase("y")) {
                    theOutput = "Knock! Knock!";
                    if (currentJoke == (NUMJOKES - 1))
                        currentJoke = 0;
                    else
                        currentJoke++;
                    state = SENTKNOCKKNOCK;
                } else {
                    theOutput = "Bye.";
                    state = WAITING;
                }
            }
            return theOutput;
        }
    }
    public static void main(String[] args) {
        int portNumber = Integer.parseInt(args[0]);

        try(
            ServerSocket ServerSocket = new ServerSocket(portNumber);
            Socket client = ServerSocket.accept();
            PrintWriter out = new PrintWriter(
                client.getOutputStream(),true
            );

            BufferedReader inBuffer = new BufferedReader(
                new InputStreamReader(client.getInputStream())
            );
        ){
            
            String inputLine, outputLine;

            KnockKnockProtocol kkp = new ServerJava.KnockKnockProtocol();
            outputLine = kkp.processInput(null);
            out.println(outputLine);

            while((inputLine=inBuffer.readLine()) != null){
                outputLine = kkp.processInput(inputLine);
                out.println(outputLine);
                if (outputLine.equals("Bye.")) break;
            }
        }catch (Exception e){
            System.err.println(e.getStackTrace());
        }
    }
}