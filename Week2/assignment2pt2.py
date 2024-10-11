# class for Product
class Product: 
    # constructor for Product
    def __init__(self, name, price): 
        # assigning name to self.name
        self.name = name 
        # assigning price to self.price
        self.price = price 

# create an instance of Product with name "Item 1" and price 200.0
product1 = Product("1", 200.0) 
# create an instance of Product with name "2" and price 400.0
product2 = Product("2", 400.0) 
# create an instance of Product with name "3" and price 600.0
product3 = Product("3", 600.0) 

# class for Catalog
class Catalog: 
    # constructor for Catalog
    def __init__(self, products): 
        # assigning products to self.products
        self.products = products 

    # method to print a combo of two products with a discount
    def print_combo(self, combo_number, product1, product2, discount):
        combo_price = (product1.price + product2.price) * discount
        combo = f"Combo {combo_number}(Item {product1.name}+{product2.name})"
        print(f"{combo:<25}{combo_price:>10.1f}")

    # method to print the catalog
    def print_catalog(self): 
        # print the store name
        print("Online Store") 
        # print a separator
        print("-------------------") 

        print(f"{'Product':<25}{'Price':>10}")
        # iterate over the products in the catalog
        for product in self.products: 
            # define the item name
            item = f"Item {product.name}"
            # print the name and price of each product
            print(f"{item:<25}{product.price:>10.1f}") 

        # call the print_combo method with the first two products with a 10% discount
        self.print_combo(1, self.products[0], self.products[1], 0.9) 
        # call the print_combo method with the last two products with a 10% discount
        self.print_combo(2, self.products[1], self.products[2], 0.9) 
        # call the print_combo method with the first and last products with a 10% discount
        self.print_combo(3, self.products[0], self.products[2], 0.9) 

        # calculate the total price of all products with a 25% discount
        total_price = (self.products[0].price + self.products[1].price + self.products[2].price) * 0.75

        # define a combo of all three products
        combo = f"Combo 4(Item {self.products[0].name}={self.products[1].name}+{self.products[2].name})"

        # print the total price of all products with a 25% discount
        print(f"{combo:<25}{total_price:>10.1f}")

        # print a separator
        print("-------------------")
        # print the delivery contact information
        print("For delivery contact: 98764678899")

# create an instance of Catalog with the three products
catalog = Catalog([product1, product2, product3])

# call the print_catalog method of the catalog instance
catalog.print_catalog()

# Formatting explanation:

# The :<25 and :>10.1f formatting options ensure that the product names are left-aligned within a 25-character wide column and the prices are right-aligned within a 10-character wide column with two decimal places.

print(17)


print(float((60*100)/55))