import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class JavaList {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        List<Integer> arr = new ArrayList<>();
    
        for (int i = 0; i < n; i++) {
            arr.add(scanner.nextInt());
        }
        
        int num_op = scanner.nextInt();
        for (int i = 0; i < num_op; i++) {
            String op = scanner.next();
            if (op.equals("Insert")) {
                int x = scanner.nextInt();
                int y = scanner.nextInt();
                arr.add(x, y);
            } else if (op.equals("Delete")) {
                int x = scanner.nextInt();
                arr.remove(x);
            }
        }
        
        for (int num: arr) {
            System.out.print(num + " ");
        }
        
        scanner.close();
    }
}