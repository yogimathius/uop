package cs1102.week2.librarymanagement;

import java.util.Scanner;

public class LibraryManagementSystem {
   public static void main(String[] args) {
       Library library = new Library();
       Scanner scanner = new Scanner(System.in);


       while (true) {
           System.out.println("\n=== Library Management System ===");
           System.out.println("1. Add Books");
           System.out.println("2. Borrow Books");
           System.out.println("3. Return Books");
           System.out.println("4. Exit");
           System.out.print("Enter your choice: ");


           int choice;
           try {
               choice = Integer.parseInt(scanner.nextLine());
           } catch (NumberFormatException e) {
               System.out.println("Please enter a valid number!");
               continue;
           }


           switch (choice) {
               // add book
               case 1:
                   System.out.print("Enter book title: ");
                   String title = scanner.nextLine();
                   System.out.print("Enter author name: ");
                   String author = scanner.nextLine();
                   System.out.print("Enter quantity: ");
                   try {
                       // parse the quantity to an integer
                       int quantity = Integer.parseInt(scanner.nextLine());
                       // check if the quantity is positive
                       if (quantity <= 0) {
                           System.out.println("Quantity must be positive!");
                           break;
                       }
                       library.addBook(title, author, quantity);
                   } catch (NumberFormatException e) {
                       System.out.println("Please enter a valid number!");
                   }
                   break;


               // borrow book
               case 2:
                   System.out.print("Enter book title: ");
                   title = scanner.nextLine();
                   System.out.print("Enter quantity to borrow: ");
                   try {
                       int borrowQuantity = Integer.parseInt(scanner.nextLine());
                       // check if the quantity is positive
                       if (borrowQuantity <= 0) {
                           System.out.println("Quantity must be positive!");
                           break;
                       }
                       library.borrowBook(title, borrowQuantity);
                   } catch (NumberFormatException e) {
                       System.out.println("Please enter a valid number!");
                   }
                   break;


               // return book
               case 3:
                   System.out.print("Enter book title: ");
                   title = scanner.nextLine();
                   System.out.print("Enter quantity to return: ");
                   try {
                       int returnQuantity = Integer.parseInt(scanner.nextLine());
                       // check if the quantity is positive
                       if (returnQuantity <= 0) {
                           System.out.println("Quantity must be positive!");
                           break;
                       }
                       library.returnBook(title, returnQuantity);
                   } catch (NumberFormatException e) {
                       System.out.println("Please enter a valid number!");
                   }
                   break;


               // exit
               case 4:
                   System.out.println("Thank you for using the Library Management System!");
                   scanner.close();
                   System.exit(0);


               default:
                   System.out.println("Invalid choice! Please try again.");
           }
       }
   }
}
