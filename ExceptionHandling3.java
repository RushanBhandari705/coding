
import java.util.Scanner;
public class ExceptionHandling3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first number: ");
        try {
        int num1 = sc.nextInt();
        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();
        System.out.println("The sum is: " + (num1 + num2));
        } 
        catch(Exception e) {
            System.out.println("Invalid input! Please enter integers only.");  
        }
        System.out.println("hello world");

        sc.close();
    }
}

