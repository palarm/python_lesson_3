# Тип данных словари

    # Инициализация

dict_temp = {}
print(type(dict_temp))

dict_temp = {'dict1': 1, 'dict2': 2.1, 'dict3': 'name', 'dict4': [1,2,3]}
print(type(dict_temp), dict_temp)

dict_temp = dict.fromkeys(['a', 'b'], [12, 2020])
print(type(dict_temp), dict_temp)

dict_temp = dict(brend = 'Volvo', volume_engine = 1.5)
print(type(dict_temp), dict_temp)

dict_temp = {a: a**2 for a in range(10)} # генерация с наполнением квадратами числа
print(type(dict_temp), dict_temp)

#     # Обращене к содержимому словаря
#
# # print(dict_temp['brend'])  # регистрочувствительный к ключу
# print(dict_temp[8])

#     # Функции со словарем
# print()
# print()
# print(dict_temp.keys())
# print(list(dict_temp.keys()))
# print(dict_temp.values())
print(dict_temp.items())

    # Работа с элементами

dict_temp[0] = 100
print(type(dict_temp), dict_temp)

dict_temp['name'] = 'dkfjsldfjk'
print(type(dict_temp), dict_temp)
# #Кортеж - () это неизменяемый list (иначе - список)
    # Методы

temp = dict_temp.pop('name') # Удаление значения по ключу
print(temp)
print(type(dict_temp), dict_temp)

    # Итерирование (прохожение) по словарю

for pair in dict_temp.items():
    print(pair)

for key, value in dict_temp.items():
    print(key, value)

for key in dict_temp.keys():
    print(key)

for value in dict_temp.values():
    print(value)


