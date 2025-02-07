class Shop:
    products = {'молоко': 10, 'колбаса': 20, 'йогурт': 30}
    discounted_products = ['молоко']
    def __init__(self):
        self.count = 0
        self.all_sum = 0



    def buy(self, prod):
        if prod in self.products:
            price = self.products[prod]
            if prod in self.discounted_products:
                price -= 5
            self.count += 1
            self.all_sum += 1
            print(f'купили {self.products[prod]}')
        else:
            print('такого нет')

    def add_product(self, product, price):
        self.products[product] = price
        print('обновили базу')

    def get_info(self):
        print(f'всего купили на {self.all_sum}р')
        print(f'всего чеков {self.count}')
        print('хорошего дня')

    def check_discount(self, product):
        return product in self.discounted_products


    def delete_product(self, product):
        if product in self.products:
            self.products.pop(product)
        else:
            print("Товар не найден.")


shop = Shop()
shop.buy('колбаса')
shop.buy('колбаса')
shop.buy('яйца')
shop.add_product('яйца', 100)
shop.buy('яйца')
shop.get_info()
shop.check_discount('печеньки')
shop.delete_product('сосиски')
print(shop.products)

