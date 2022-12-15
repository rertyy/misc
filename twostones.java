import java.util.*;

public class twostones {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        int number = Integer.parseInt(input);
        String winner;
        if ( number % 2 == 1) {
            winner = "Alice";
        } else {
            winner = "Bob";
        }
        System.out.println(winner);
        sc.close();
    }
}