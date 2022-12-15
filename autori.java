import java.util.*;

public class autori {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine(); //reads the next line the user inputs and assign it to String input
        
        int len = input.length();
        String output = "";
        
        for (int i = 0; i < len; i++) {
            if (input.charAt(i) > 64 && input.charAt(i) < 91) {
                output+=input.charAt(i);
            }
        }
        
        System.out.println(output); //prints ...
        sc.close(); //impt to close scanner afterwards!
    }
}