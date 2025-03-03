import java.util.Scanner;

public class JavaAnagrams {

    static boolean isAnagram(String a, String b) {
        a = a.toLowerCase();
        b = b.toLowerCase();
        
        if (a.length() != b.length()) return false;
        
        char[] a_array = a.toCharArray();
        char[] b_array = b.toCharArray();
        
        java.util.Arrays.sort(a_array);
        java.util.Arrays.sort(b_array);
        
        return java.util.Arrays.equals(a_array, b_array);
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}