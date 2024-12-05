package cs1102.week3.studentmanagement;

public class Main {
    public static void main(String[] args) {
        StudentManagement studentManagement = new StudentManagement();
        AdminInterface adminInterface = new AdminInterface(studentManagement);
        adminInterface.run();
    }
}
