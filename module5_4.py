class House:
    houses_history = []  # Атрибут класса для хранения названий объектов

    def __new__(cls, *args, **kwargs):
        # Добавляем название дома в историю
        if args:  # Проверяем, были ли переданы аргументы
            cls.houses_history.append(args[0])
        return super().__new__(cls)  # Вызываем метод __new__ родительского класса

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"


# Пример использования класса
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # Проверяем историю

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # Проверяем историю

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # Проверяем историю

# Удаление объектов
del h2
del h3

print(House.houses_history)  # Проверяем историю после удаления

# Удаление h1 последним
del h1