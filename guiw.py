import tkinter as tk
import customtkinter as ctk
import json

class cart(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_2 = ctk.CTkLabel(self, text="Cart", font=("Arial", 15))
        self.label_2.grid(row=0, column=0, pady=10, sticky="ew")

        self.update_cart()

    def update_cart(self):
        for widget in self.winfo_children():
            widget.destroy()

        with open("client/json/item/cart.json", "r") as file:
            data = json.load(file)
            for idx, item in enumerate(data):
                self.label = ctk.CTkLabel(self, text=f"{item}\nPrice: {data[item]['price']}\nQuantity: {data[item]['quantity']}")
                self.label.grid(row=idx, column=0, pady=5, sticky="ew")


class Product(ctk.CTkFrame):
    def __init__(self, master, product: dict, update_cart_callback):
        super().__init__(master)
        self.grid_columnconfigure((0), weight=1)
        
        self.label_1 = ctk.CTkLabel(self, font=("Arial", 15))
        self.label_1.configure(text=f"{product['name']}\nPrice: {product['price']}")
        self.label_1.grid(row=0, column=0, pady=10, sticky="ew")

        self.button_cart = ctk.CTkButton(master=self, fg_color="transparent", hover_color="grey10", border_width=0,
                                           text_color=("gray10", "#DCE4EE"), text="Add to cart",
                                           command=lambda: self.add_to_cart(product, update_cart_callback))
        self.button_cart.grid(row=0, column=1, padx=20, pady=(20, 20))

    def add_to_cart(self, product, update_cart_callback):
        with open("client/json/item/cart.json", "r") as file:
            data = json.load(file)
        try:
            data[product["name"]]["quantity"] += 1
        except KeyError:
            data[product["name"]] = {"price": product["price"], "quantity": 1}
        with open("client/json/item/cart.json", "w") as file:
            json.dump(data, file)
        update_cart_callback()  # Update the cart display

class MainPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.grid_columnconfigure((0), weight=1)

        self.title("ABC Supermarket")
        self.geometry(f"{720}x{540}")
        self.grid_columnconfigure(0, weight=1)

        self.label_title = ctk.CTkLabel(self, text="Mainpage", font=("Arial", 20))
        self.label_title.grid(row=0, column=0, pady=10, sticky="ew")

        self.tabview_1 = ctk.CTkTabview(self, height=400, width=700)
        self.tabview_1.add("Browse Product")
        self.tabview_1.tab("Browse Product").grid_columnconfigure(0, weight=1)
        self.tabview_1.add("Cart")
        self.tabview_1.tab("Cart").grid_columnconfigure(0, weight=1)
        self.tabview_1.add("Shopping History")
        self.tabview_1.set("Browse Product")
        self.tabview_1.grid(row=1, column=0, padx=20, pady=(20, 20))

        self.label_1 = ctk.CTkLabel(self.tabview_1.tab("Browse Product"), text="Product List\n", font=("Arial", 15))
        self.label_1.grid(row=0, column=0, pady=10, sticky="ew")

        self.cart = cart(self.tabview_1.tab("Cart"))
        self.cart.grid(row=0, column=0, pady=10, sticky="ew")

        with open("client/json/item/item.json", "r") as file:
            self.data = json.load(file)
            for idx, item in enumerate(self.data):
                Product(self.tabview_1.tab("Browse Product"), self.data[item], self.cart.update_cart).grid(row=idx + 1, column=0, pady=5, sticky="ew")
        
if __name__ == "__main__":
    gui = MainPage()
    gui.mainloop()
