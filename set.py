# Тип данных множество

    # Инициализация
#
# temp_set = {}  # пустые скобки это dict - словарь
# temp_set = {1, 2, 3}  # наполненные  фигурные скобки это set
# print(type(temp_set), temp_set)
# temp_list = [1, 2, 1, 2, 1, 2, 2, 3, 12, 34]
# temp_set = set(temp_list)
# print(type(temp_set), temp_set)
#
#     # Обращение к элементам множества
#
# print(1 in temp_set)
# print(100 in temp_set)
#
# for i in temp_set:
#     print(i)

    # Функции с множествами

# Функции те же

    # Операции с множествами

my_set_1 = set([1, 2, 3, 4, 5])
my_set_2 = set([5, 6, 7, 8, 9])

my_set_3 = my_set_1.union(my_set_2)
print(my_set_3)

my_set_4 = my_set_1.difference(my_set_2)
print(my_set_4)

    # Методы