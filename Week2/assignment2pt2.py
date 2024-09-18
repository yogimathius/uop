
"""

Part 2
Welcome to your first project.  Develop a catalog for a company. Assume that this company sells three different Items. The seller can sell individual items or a combination of any two items. A gift pack is a special combination that contains all three items. Here are some special considerations:  

A. If a customer purchases individual items, he does not receive any discount.  
B. If a customer purchases a combo pack with two unique items, he gets a 10% discount.  
C. If the customer purchases a gift pack, he gets a 25% discount. 

Write a function for the above scenario. Perform the calculations in code wherever applicable.  The function should be your own creation, not copied from any other source.  The final output should look like: 

Output of online store


Include the following in your part 2 submission:

The code for the function that you created. 
The Output of the code. 
A description of what feature(s) your function illustrates.
The code and its output must be explained technically. The explanation can be provided before or after the code, or in the form of comments within the code. 
If you use an informational source, be sure to identify the source and share the link to the source you used. 

Submission Instructions:  
Submit the solutions to both part 1 and part 2 in one document.
Make sure your submission is double-spaced, using Times New Roman, 12-point font, with 1” margins.   
The descriptive part of your response must be at least 200 words.
Use sources to support your arguments. Use high-quality, credible, relevant sources to develop ideas that are appropriate for the discipline and genre of the writing.  
Use APA citations and references to support your work. Add a reference list at the end of the submission. For assistance with APA formatting, view the Learning Resource Center: Academic Writing.  
Your submission should be clearly written, concise, well organized, and free of spelling and grammar errors. The grading will be based on an accurate solution to the problem and the quality of your writing. 
"""
class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price

product1 = Product("Item 1", 200.0)
product2 = Product("Item 2", 400.0)
product3 = Product("Item 3", 600.0)

class Catalog:
    def __init__(self, products):
        self.products = products

    def print_catalog(self):
        print("Online Store")
        print("-------------------")
        for product in self.products:
            print(product.name, product.price)
        print("Combo 1: ", self.products[0].name, " + ", self.products[1].name, " = ", (self.products[0].price + self.products[1].price) * 0.9)
        print("Combo 2: ", self.products[1].name, " + ", self.products[2].name, " = ", (self.products[1].price + self.products[2].price) * 0.9)
        print("Combo 3: ", self.products[0].name, " + ", self.products[2].name, " = ", (self.products[0].price + self.products[2].price) * 0.9)
        print("Combo 4: ", self.products[0].name, " + ", self.products[1].name, " + ", self.products[2].name, " = ", (self.products[0].price + self.products[1].price + self.products[2].price) * 0.75)
        print("-------------------")
        print("For delivery contact: 98764678899")


catalog = Catalog([product1, product2, product3])

catalog.print_catalog()