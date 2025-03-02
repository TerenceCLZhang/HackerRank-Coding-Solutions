import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class JavaEndOfFile {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int lineNum = 1;
        while (scanner.hasNext()) {
            String input = scanner.nextLine();
            System.out.printf("%d %s\n", lineNum, input);
            lineNum++;
        }
    }
}