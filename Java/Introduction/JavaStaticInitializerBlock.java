import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class JavaStaticInitializerBlock {

static int B, H;
static boolean flag = true;

static {
    Scanner scanner = new Scanner(System.in);
    B = scanner.nextInt();
    H = scanner.nextInt();
    scanner.close();
    
    if (B <= 0 || H <= 0) {
        System.out.println("java.lang.Exception: Breadth and height must be positive");
        flag = false;
    }
}

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class

