import java.util.*;

public class timeloop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        int max = Integer.parseInt(input);
        for (int i = 1; i <= max; i++) {
            System.out.printf("%d Abracadabra \n", i);
        }
        sc.close();
    }
}