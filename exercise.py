import re
import pymorphy2


# LIGHT:
# 0) cчитать/скопировать текст из файла

draft_line = []
with open('text.txt', encoding='utf-8') as f:
    for line in f:
        draft_line.append(line)

print(draft_line)


# 1) методами строк очистить текст от знаков препинания;
# 2) сформировать list со словами (split);

# Вариант 1.1 ord() c испозованием строк
# учитывает только кириллицу, не анализирует "Ё" и "ё"

# clear_list = []
#
# for new_str in draft_line:
#     new_str_list = list(new_str)
#     #print(new_str)
#
#     for i in range(len(new_str_list)):
#         temp_symbol = ord(new_str_list[i])
#         if ( temp_symbol < 1040 or temp_symbol > 1103) and temp_symbol != 32:
#             new_str_list[i] = chr(32) # если символ не в кириллическом диапазоне, заменяем на пробел
#
#     new_str = ''.join(new_str_list)
#     clear_list += new_str.split()
#     print(new_str)
#
# print(clear_list)

# Вариант 1.2 ord() c испозованием строк
# учитывает только кириллицу, не анализирует "Ё" и "ё"

# clear_list = []
# temp_word = ""
#
# for string in draft_line:
#
#     for i in string:
#         if ord(i) > 1039 and ord(i) < 1104:
#             temp_word += i
#         else:
#             if temp_word != "":
#                 clear_list.append(temp_word)
#                 temp_word = ""
#
# print(clear_list)

# Вариант 1.3 с предопределенным списком знаков препинания

# symbol_list = [' ','.',',','?','!','-','–','—',"'",'"','«','»',':',';','(',')','\n']
# clear_list = []
#
# for string in draft_line:
#     for a in range(len(symbol_list)):
#         string = string.replace(symbol_list[a], ' ')
#     clear_list += string.split()
# print(clear_list)

# Вариант 1.4 с использованием findall()

clear_list = []

for string in draft_line:
    clear_list += (re.findall(r'\w+', string))
print(clear_list)

# 3) привести все слова к нижнему регистру (map);

# # Вариант 3.1 через строковый lower()
# lower_list = []
#
# for string in clear_list:
#     lower_list.append(string.lower())
# print(lower_list)

# Вариант 3.2 через map с использованием lambda
#lower_list = []

lower_list = list(map(lambda x: x.lower(), clear_list))

print(lower_list)

# 4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;

#dict_from_lower_list = {}
dict_from_lower_list = {x: lower_list.count(x) for x in lower_list}

print(dict_from_lower_list)

# 5) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

list_of_tuple_by_item = list(dict_from_lower_list.items())
list_of_tuple_by_item.sort(key=lambda i: i[1], reverse=True)

print(list_of_tuple_by_item[:5])
print(len(set(dict_from_lower_list)))

# PRO:
# 6) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.

morph = pymorphy2.MorphAnalyzer()
t = []

for i in lower_list:
    if len(i) > 2: # можно дополнительно отбросить предлоги и междометия как не существенные для обработки
        t.append(morph.parse(i)[0].normal_form)

print(t)