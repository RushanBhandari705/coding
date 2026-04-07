import java.util.Scanner;

public class Work {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your age: ");
        try {
            int age = scanner.nextInt();
            if (age < 18) {
                throw new IllegalArgumentException("Age should be at least 18");
            }
            System.out.println("Age is greater than 18");
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please enter a valid integer.");
        } finally {
            System.out.println("Good Boy");
        }
        scanner.close();
    }
}
