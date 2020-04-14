# Тип данных строка

    # Инициализация

temp_str = 'Марка авто "Volvo"'
#temp_str = ""
print(temp_str)

    # Обращение к символам, подстрокам
# Вывод строки посимвольно
for i in range(len(temp_str)):
    print(temp_str[i])
# Срезы
print(temp_str[1:])
print(temp_str[:4])
print(temp_str[1:4])
print(temp_str[1:-3])

    # Функции со строками

print(temp_str, len(temp_str))

    # Операции со строками

temp_str_2 = 'Mercedes'
print(temp_str + temp_str_2)
print(temp_str_2*2)

    # Форматирование строк

brand = 'Volvo'
price = 1.7

car = 'Марка {} цена {}'.format('Volvo', 1.5)
car2 = 'Марка {} цена {}'.format(brand, price) # Для версии 2.х
car3 = f'Марка {brand} цена {price}' # Для версии 3.х

print(car)
print(car2)
print(car3)

    # Методы

print(temp_str.split())
cars = 'Volvo,Audi,Lada'
print(cars.split())
print(cars.split(','))

# Методы форматирования строк

print(cars.upper())
print(cars.title())
print(cars.lower())

# Замена подстроки в строке

email_adress = 'eMail: _mail_'
email = '123@123.om'
print(email_adress.replace('_mail_', email))




