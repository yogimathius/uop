package cs1102.week3.studentmanagement;

import java.util.Scanner;

public class AdminInterface {
  private StudentManagement studentManagement;
  public enum AdminInterfaceChoice {
    ADD_STUDENT,
    REMOVE_STUDENT,
    DISPLAY_ALL_STUDENTS,
    SEARCH_STUDENT,
    UPDATE_STUDENT,
    EXIT
  }
  public AdminInterface(StudentManagement studentManagement) {
    this.studentManagement = studentManagement;
  }

  public void displayMenu() {
    System.out.println("1. Add Student");
    System.out.println("2. Remove Student");
    System.out.println("3. Display All Students");
    System.out.println("4. Search Student");
    System.out.println("5. Update Student");
    System.out.println("6. Exit");
  } 

  public void run() {
    Scanner scanner = new Scanner(System.in);
    while (true) {
      displayMenu();
      int choice = scanner.nextInt();
      scanner.nextLine();
      AdminInterfaceChoice adminInterfaceChoice = AdminInterfaceChoice.values()[choice - 1];

      switch (adminInterfaceChoice) {
        case ADD_STUDENT:
          this.studentManagement.addStudent(getStudentFromInput(scanner));
          break;

        case REMOVE_STUDENT:
          System.out.println("Enter student ID: ");
          this.studentManagement.removeStudent(scanner.nextInt());
          scanner.nextLine();
          break;

        case DISPLAY_ALL_STUDENTS:
          this.studentManagement.displayAllStudents();
          break;

        case SEARCH_STUDENT:
          System.out.println("Enter student ID: ");
          this.studentManagement.searchStudent(scanner.nextInt());
          scanner.nextLine();
          break;

        case UPDATE_STUDENT:
          System.out.println("Enter student ID: ");
          int id = scanner.nextInt();
          scanner.nextLine();
          System.out.println("Enter student name: ");
          String name = scanner.nextLine();
          System.out.println("Enter student age: ");
          int age = scanner.nextInt();
          scanner.nextLine();
          System.out.println("Enter student grade: ");
          String grade = scanner.nextLine();
          this.studentManagement.updateStudent(id, name, age, grade);
          scanner.nextLine();
          break;


        case EXIT:
          System.out.println("Exiting...");
          scanner.close();
          return;
      }
    }

  }
  
  private Student getStudentFromInput(Scanner scanner) {
    System.out.println("Enter student ID: ");
    int id = scanner.nextInt();
    scanner.nextLine();
    System.out.println("Enter student name: ");
    String name = scanner.nextLine();
    System.out.println("Enter student age: ");
    int age = scanner.nextInt();
    scanner.nextLine();
    System.out.println("Enter student grade: ");
    String grade = scanner.nextLine();
    return new Student(id, name, age, grade);
  }
}
