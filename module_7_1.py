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
        self.__file_name = open(self.__file_name, 'a')
        self.__file_name.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        name_prod = file.read()
        file.close()
        return name_prod

    def add(self, *products):
        existing_products = {}
        file = open(self.__file_name, 'r')
        for i in file:
            name, weight, category = i.strip().split(', ')
            existing_products[(name, category)] = float(weight)
        file.close()



