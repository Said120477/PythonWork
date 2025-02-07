class Shop:
    products = {'молоко': 10, 'колбаса': 20, 'сосиски': 50}
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Store:
    def __init__(self):
        self.products = []
        self.discounted_products = []
    def add_product(self, product):
        self.products.append(product)
    def add_discounted_product(self, product):
        self.discounted_products.append(product)
    def _check_discount(self, product):
        if product in self.discounted_products:
            product.price -= 5
    def purchase(self, product):
        self._check_discount(product)
        print(f"Покупка: {product.name}, Цена после скидки: {product.price} руб.")
    def delete_product(self, product):
        if product in self.products:
            self.products.remove(product)
        if product in self.discounted_products:
            self.discounted_products.remove(product)
            print(f"Товар {product.name} удален из базы данных.")
        else:
            print("Товар не найден.")

store = Store()
item1 = Shop("Товар 1", 100)
item2 = Shop("Товар 2", 150)
store.add_product(item1)
store.add_product(item2)
store.add_discounted_product(item1)
store.purchase(item1)
store.delete_product(item1)