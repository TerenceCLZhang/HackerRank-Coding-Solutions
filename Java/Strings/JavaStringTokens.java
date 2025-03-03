import java.io.*;
import java.util.*;

public class JavaStringTokens {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine().trim();
        
        String[] tokens = s.split("[ !,?._'@]+");
        
        if (s.isEmpty()) System.out.println(0);
        else System.out.println(tokens.length);
        
        for (String token: tokens) System.out.println(token);
        
        scan.close();
    }
}

