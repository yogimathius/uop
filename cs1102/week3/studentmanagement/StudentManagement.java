package cs1102.week3.studentmanagement;

import java.util.ArrayList;
import java.util.List;

public class StudentManagement {
  private List<Student> students;

  public StudentManagement() {
    this.students = new ArrayList<>();
  }

  public void addStudent(Student student) {
    if (findStudentById(student.getId()) != null) {
      System.out.println("Student already exists!");
      return;
    }
    this.students.add(student);
    System.out.println("Student added successfully!");
  }

  public void removeStudent(int id) {
    Student student = findStudentById(id);
    if (student != null) {
      students.remove(student);
      System.out.println("Student removed successfully!");
    } else {
      System.out.println("Student not found!");
    }
  }

  public void displayAllStudents() {
    for (Student s : students) {
      System.out.println(s.getId() + " " + s.getName() + " " + s.getAge() + " " + s.getGrade());
    }
  }

  public void searchStudent(int id) {
    Student student = findStudentById(id);
    if (student != null) {
      System.out.println(student.getId() + " " + student.getName() + " " + student.getAge() + " " + student.getGrade());
    } else {
      System.out.println("Student not found!");
    }
  }

  public void updateStudent(int id, String name, int age, String grade) {
    Student student = findStudentById(id);
    if (student != null) {
      student.setName(name);
      student.setAge(age);
      student.setGrade(grade);
      System.out.println("Student updated successfully!");
    } else {
      System.out.println("Student not found!");
    }
  }

  private Student findStudentById(int id) {
    for (Student s : students) {
      if (s.getId() == id) {
        return s;
      }
    }
    return null;
  }
}
