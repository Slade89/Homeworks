class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    # def go_to(self, new_floor):
    #     floor = 0
    #     if new_floor > self.number_of_floors or new_floor < 1:
    #         print("Такого этажа не существует")
    #     else:
    #         for floor in range(new_floor):
    #             print(floor + 1)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# h1.go_to(5)
# h2.go_to(10)
print(h1)
print(h2)
print(len(h1))
print(len(h2))