class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price):
        self.cart[item] = price
        print(item, "added to cart.")

    def remove_item(self, item):
        if item in self.cart:
            del self.cart[item]
            print(item, "removed from cart.")
        else:
            print("Item not found.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            total = 0
            for item, price in self.cart.items():
                print(f"{item} - ₱{price}")
                total += price
            print("Total: ₱", total)

    def checkout(self):
        total = sum(self.cart.values())
        print("\nCheckout successful!")
        print("Total amount to pay: ₱", total)
        self.cart.clear()


cart = ShoppingCart()

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart.add_item(item, price)

    elif choice == "2":
        item = input("Enter item name to remove: ")
        cart.remove_item(item)

    elif choice == "3":
        cart.view_cart()

    elif choice == "4":
        cart.checkout()

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice.")