import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class JavaArraylist {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int num_of_ints = scanner.nextInt();
            ArrayList<Integer> ints = new ArrayList<>();
            for (int j = 0; j < num_of_ints; j++) {
                ints.add(scanner.nextInt());
            }
            arr.add(ints);
        }

        int num_queries = scanner.nextInt();
        for (int i = 0; i < num_queries; i++) {
            int x = scanner.nextInt() - 1;
            int y = scanner.nextInt() - 1;

            try {
                System.out.println(arr.get(x).get(y));
            } catch (IndexOutOfBoundsException e) {
                System.out.println("ERROR!");
            }
        }

        scanner.close();
    }
}