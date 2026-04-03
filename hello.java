import java.util.Scanner;

public class hello {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the age:");
        try {
            int age = scanner.nextInt();
            if (age > 18) {
                throw new IllegalArgumentException("Age should be atleast 18");
            }
            System.out.println("Age is greater than 18");
        } catch (IllegalArgumentException e) {
            System.out.println("error:" + e.getMessage());
        } catch (Exception e) {
            System.out.println("Error: Invalid input");
        } finally {
            System.out.println("GoodBoy");
        }
        scanner.close();
    }
}
