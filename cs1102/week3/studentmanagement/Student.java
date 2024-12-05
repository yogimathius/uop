package cs1102.week3.studentmanagement;

public class Student {
  private int id;
  private String name;
  private int age;
  private String grade;

  public Student(int id, String name, int age, String grade) {
    this.id = id;
    this.name = name;
    this.age = age;
    this.grade = grade;
  }

  public int getId() {
    return id;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
  }

  public String getGrade() {
    return grade;
  }

  public void setGrade(String grade) {
    this.grade = grade;
  }
}
