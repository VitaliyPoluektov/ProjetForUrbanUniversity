class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        product_str = str(f'{self.name}, {self.weight}, {self.category}')
        return product_str

class Shop:
    __file_name = 'products.txt'
    def __init__(self):
        file = open(self.__file_name, 'a')
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        name_prod = file.read()
        file.close()
        return name_prod

    def add(self, *products):
        product = self.get_products()
        existing_products = {}
        if product != '':
            productss = product.strip().split('\n')
            for l in productss:
                name, weight, category = l.strip().split(', ')
                existing_products[(name, category)] = float(weight)
        file = open(self.__file_name, 'a')
        for p in products:
            key = (p.name, p.category)
            if key in existing_products:
                    existing_products[key] += p.weight
                    print(
                        f'Продукт {p.name} уже был в магазине, его общий вес теперь'
                        f' равен {existing_products[key]}.')
            else:
                    existing_products[key] = p.weight
            file.write(f'{p.name}, {existing_products[key]}, {p.category}\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())