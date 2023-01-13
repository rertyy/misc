import java.util.*;

public class lastfactorialdigit {
    public static void main(String[] args) {
        // int lmao = 5;
        Scanner sc = new Scanner (System.in);
        int numberOfResults = sc.nextInt();
        for (int i = 0; i < numberOfResults; i++) {
            int toCompute = sc.nextInt();
            switch (toCompute) {
                case 1:
                case 2:
                case 4:
                    System.out.println(toCompute);
                    break;
                case 3:
                    System.out.println(6);
                    break;
                default:
                    System.out.println(0);
            }
        }
        
        sc.close();
    }
}