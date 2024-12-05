package cs1102.week2.librarymanagement;

import java.util.ArrayList;
import java.util.List;


public class Library {
   private List<Book> books;


   public Library() {
       this.books = new ArrayList<>();
   }


   public void addBook(String title, String author, int quantity) {
       for (Book book : books) {
           // if the book already exists, update the quantity and return
           if (book.getTitle().equalsIgnoreCase(title)) {
               book.setQuantity(book.getQuantity() + quantity);
               System.out.println("Book quantity updated successfully!");
               return;
           }
       }
       // if the book does not exist, add it to the library
       books.add(new Book(title, author, quantity));
       System.out.println("Book added successfully!");
   }


   public void borrowBook(String title, int quantity) {
       for (Book book : books) {
           // if the book exists, check if the quantity is available and borrow it
           if (book.getTitle().equalsIgnoreCase(title)) {
               if (book.getQuantity() >= quantity) {
                   book.setQuantity(book.getQuantity() - quantity);
                   System.out.println("Books borrowed successfully!");
                   return;
               } else {
                   // if the quantity is not available, print a message and return
                   System.out.println("Insufficient books available!");
                   return;
               }
           }
       }
       // if the book does not exist, print a message and return
       System.out.println("Book not found in library!");
   }


   public void returnBook(String title, int quantity) {
       for (Book book : books) {
           // if the book exists, add the quantity to the book
           if (book.getTitle().equalsIgnoreCase(title)) {
               book.setQuantity(book.getQuantity() + quantity);
               System.out.println("Books returned successfully!");
               return;
           }
       }
       // if the book does not exist, print a message and return
       System.out.println("Book does not belong to this library!");
   }
}

