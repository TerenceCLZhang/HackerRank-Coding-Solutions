import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;

// Replace "JavaSingletonPattern" with "Singleton" for submission.

class JavaSingletonPattern{
    private static JavaSingletonPattern obj;
    private JavaSingletonPattern() {}
    public String str;
    
    public static JavaSingletonPattern getSingleInstance() {
        if (obj == null) obj = new JavaSingletonPattern();
        return obj;
    }
}