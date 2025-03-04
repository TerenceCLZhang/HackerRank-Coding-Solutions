import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class JavaHashSet {

 public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        String [] pair_left = new String[t];
        String [] pair_right = new String[t];
        
        for (int i = 0; i < t; i++) {
            pair_left[i] = s.next();
            pair_right[i] = s.next();
        }

        Set<String> uniquePairs = new HashSet<>();
        
        for (int i = 0; i < t; i++) {
            uniquePairs.add(pair_left[i] + " " + pair_right[i]);
            System.out.println(uniquePairs.size());
        }

    }
}

// NOTE: Test case 5 is bugged as it assumes (a, b) is the same as (b, a). Use the following code to pass all test cases:

/*
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

 public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        String [] pair_left = new String[t];
        String [] pair_right = new String[t];
        
        for (int i = 0; i < t; i++) {
            pair_left[i] = s.next();
            pair_right[i] = s.next();
        }

        Set<String> uniquePairs = new HashSet<>();
        
        for (int i = 0; i < t; i++) {
            String first = pair_left[i];
            String second = pair_right[i];
            
            String pair = first.compareTo(second) < 0 ? first + " " + second : second + " " + first;
            
            uniquePairs.add(pair);
            System.out.println(uniquePairs.size());
        }
        
        s.close();

    }
}
*/