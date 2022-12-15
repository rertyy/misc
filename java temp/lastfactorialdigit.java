import java.util.*;

public class lastfactorialdigit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine(); //reads the next line the user inputs and assign it to String input
        boolean flag;
        flag = false;
        int num = Integer.parseInt(input);
        if (flag == false) {
            flag = true;
        } else {
            switch (num) {
                case 1:
                case 2:
                case 4:
                    System.out.println(num);
                    break;
                case 3:
                    System.out.println(6);
                    break;
                default:
                    System.out.println(0);
            }
        }
        sc.close(); //impt to close scanner afterwards!
    }
}