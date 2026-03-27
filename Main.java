class Student {
    private String name = "Rushan";

    public String getName() {
        return name;
    }
}

public class Main {
    public static void main(String[] args) {
        Student s = new Student();
        System.out.println(s.getName());
    }
}