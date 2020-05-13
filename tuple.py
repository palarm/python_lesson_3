# Тип данных кортеж

#     # Инициализация
#
# temp_tuple = (1, 2, 3)
# print(type(temp_tuple), temp_tuple)
#
#     # Обращение к элементам кортежа
#
# for i in range(len(temp_tuple)):
#     print(temp_tuple[i])
#
    # Функции кортежей

# Также как в списках

#     # Операции с кортежами
#
# # Также как в списках
#
#     # Методы
temp_list = [1, 2, 3]
temp_tuple = (1, 2, 3)

print(temp_list.__sizeof__())
print(temp_tuple.__sizeof__())
#
# temp_tuple = tuple(temp_list) # преобразование листа в кортеж
# temp_list = list(temp_tuple) # преобразование кортежа в лист (для внесения изменений)

