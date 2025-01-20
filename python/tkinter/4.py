import tkinter as tk
from tkinter import messagebox

class ShoppingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping App")

        # Product list
        self.products = [
            {"name": "Product 1", "price": 19.99},
            {"name": "Product 2", "price": 29.99},
            {"name": "Product 3", "price": 39.99},
            # Add more products as needed
        ]

        # Shopping cart
        self.cart = []

        # Create widgets
        self.product_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.add_to_cart_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.view_cart_button = tk.Button(root, text="View Cart", command=self.view_cart)

        # Populate product listbox
        for product in self.products:
            self.product_listbox.insert(tk.END, f"{product['name']} - ${product['price']}")

        # Place widgets in the window
        self.product_listbox.pack(pady=10)
        self.add_to_cart_button.pack(pady=5)
        self.view_cart_button.pack(pady=10)

    def add_to_cart(self):
        selected_index = self.product_listbox.curselection()
        if selected_index:
            selected_product = self.products[selected_index[0]]
            self.cart.append(selected_product)
            messagebox.showinfo("Added to Cart", f"{selected_product['name']} added to cart.")

    def view_cart(self):
        if not self.cart:
            messagebox.showinfo("View Cart", "Your cart is empty.")
        else:
            cart_contents = "\n".join([f"{item['name']} - ${item['price']}" for item in self.cart])
            messagebox.showinfo("View Cart", f"Your Cart:\n{cart_contents}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root)
    root.mainloop()