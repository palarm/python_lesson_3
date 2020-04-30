# Типы данных список

#     # Инициализация (генераторы)
#
# list_temp = [] # Пустой список
# print(type(list_temp))
list_temp = [1.2, 123, 'Volovo', [1,2,3]]
#
# for el in list_temp:
#     print(el, type(el))

# # list
#
list_str = list('Volvo')
# print(list_str)
#
#     # Обращение к элементам списка, подсписки
# print()
# for i in range(len(list_temp)):
#     print(i, ': ', list_temp[i])
# print()
#
# for i in range(len(list_temp)):
#     print(i, ': ', list_temp[i:])
# print()
#
# for i in range(len(list_temp)):
#     print(i, ': ', list_temp[:i]) # почему теряется значение первого элемента списка??
#     # потому, что мы запрашиваем доступ от начала до i-го элемента в списке
#     # при i == 0 мы получаем значения строки до 0-го элемента НЕ ВКЛЮЧИТЕЛЬНО

#     # Функции со списками
#
# print(len(list_temp))
#

#     # Операции со списками
#
# print()
# print(list_temp + list_str)
# print(list_temp*2)

    # Методы
# append
#
# integer_list = []
#
# for i in range (10):
#     integer_list.append(i)
#
# print(integer_list)
# integer_list.append(0)
# print(integer_list)
#
# # remove
#
# integer_list.remove(0) # удаление порвого вхождения!!
# print(integer_list)
#
# del integer_list[9] # удаление по индексу
# print(integer_list)
#
# reverse
#
# integer_list.reverse() #
# print(integer_list)
#
# sort
#
integer_list = [4, 8, 3.2323, 4, 8, 1, 9, 2, 3, 5]
# print(integer_list)
# integer_list.sort()
# print(integer_list)
# #
# # # insert
#
# integer_list.insert(2,100)
# print(integer_list)

#
    # Обработка списков (map, filter, reduce)

# map


# map(function, list) ---> map ---> list(map)
new_integer_list = list(map(int, integer_list))
# print(new_integer_list)
# new_integer_list = list(map(lambda x: x**2, integer_list))
# print(new_integer_list)

# for i in range(len(new_integer_list)):
#     print(type(new_integer_list[i]), new_integer_list[i])
#
# print(new_integer_list)
# print()

# filter

# new_integer_list = list(filter(lambda x: x<5, integer_list))
# print(new_integer_list)
# print()
# print()
#
# #reduce
# from functools import reduce
# #
# integer_list = [1, 2, 3, 4]
#
# sum = reduce(lambda x,y: x+y, integer_list)
# product = reduce(lambda x,y: x*y, integer_list)
# print(sum, product)

