class Product:
    def __init__(self, name, price, availability, category):
        self.name = name
        self.price = price
        self.availability = availability
        self.category = category

    def __str__(self):
        return (f"{self.name} ({self.category}) - {self.price} руб."
                f"на складе: {self.availability} шт.")


class Order:
    def __init__(self, customer, basket):
        self.customer = customer
        self.products = basket.products
        self.total = 0
        for p in self.products:
            self.total += p["product"].price * p["quantity"]


    def apply_discount(self, percent):
        # уменшаем сумму на сколько то %
        self.total = self.total * (1 - percent / 100)

    def apply_tax(self, percent):
        # увеличиваем сумму на сколько то %
        self.total = self.total * (1 + percent / 100)


class Customer:
    def __init__(self, name, inf_customer):
        self.name = name
        self.inf_customer = inf_customer
        self.orders = [] # история заказов

    def add(self, order): # добавляем в историю заказов
        self.orders.append(order)

    def __str__(self):
        return f"Покупатель - {self.name}, история заказов - {self.orders}"


class ShoppingCart:
    def __init__(self):
        self.products = []  # корзина товаров

    def add(self, product, quantity=1):
        self.products.append({"product": product, "quantity": quantity})

    def remove(self, product):
        self.products = [p for p in self.products if p["product"] != product]

    def update(self, product, quantity):
        for p in self.products:
            if p["product"] == product:
                p["quantity"] = quantity