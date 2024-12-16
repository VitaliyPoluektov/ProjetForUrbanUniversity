class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этожа не существует')
            return
        i = 1
        while i < new_floor + 1:
            print(i)
            i += 1



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Небоскрёб', 111)
h1.go_to(5)
h2.go_to(10)
h3.go_to(0)
h3.go_to(10)