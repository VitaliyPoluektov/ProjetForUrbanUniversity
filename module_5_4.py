class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этожа не существует')
            return
        i = 1
        while i < new_floor + 1:
            print(i)
            i += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value
            return self
        elif isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        self.__add__(value)
        return self

    def __iadd__(self, value):
        self.__add__(value)
        return self

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other
        elif isinstance(other, int):
            return self.number_of_floors != other


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)



