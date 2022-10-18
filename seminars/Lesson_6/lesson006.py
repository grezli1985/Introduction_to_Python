'''
    5 Даны два файла, в каждом из которых находится запись многочлена. 
    Задача - сформировать файл, содержащий сумму многочленов.
    Коэффициенты могут быть как положительными, так и отрицательными. 
    Степени многочленов могут отличаться. '''

# polinom_1 = '5*x^2 + 3*x^6 - 15*x**3 + 66'
# polinom_2 = '13*x^3 + 3*x^4 - 15*x^8 - 99'

# polinom_1 = polinom_1.replace(' ', '').replace('**', '^').replace('*', '')
# polinom_2 = polinom_2.replace(' ', '').replace('**', '^').replace('*', '')


# def get_dict_from_polinom(str_pol):
#     lst = []
#     last_index = -1
#     neg = False
#     for i, char in enumerate(str_pol):
#         if char == '+' or char == '-':
#             if neg:
#                 lst.append('-' + str_pol[last_index + 1:i])
#             else:
#                 lst.append(str_pol[last_index + 1:i])
#             last_index = i
#             neg = char == '-'
#     if neg:
#         lst.append('-' + str_pol[last_index + 1:])
#     else:
#         lst.append(str_pol[last_index + 1:])

#     print(lst)

#     dct = {}
#     for item in lst:
#         for i, char in enumerate(item):
#             if not char.isdigit() and char != '.' and char != '-':
#                 dct[item[i:]] = float(item[:i])
#                 break
#         else:
#             dct[''] = float(item)


#     return dct        


# dct1 = get_dict_from_polinom(polinom_1)
# dct2 = get_dict_from_polinom(polinom_2)


# set1 = set(dct1.keys())
# set2 = set(dct2.keys())

# # print(set1, set2)

# # print(set1.intersection(set2))
# # print(set1.symmetric_difference(set2))

# itog_dct = {}

# for key in set1.intersection(set2):
#     itog_dct[key] = dct1[key] + dct2[key]

# for key in set1.symmetric_difference(set2):
#     if key in dct1:
#         itog_dct[key] = dct1[key]
#     else:
#         itog_dct[key] = dct2[key]

# print(itog_dct)

# print([f'{itog_dct[key]}{key}' for key in sorted(itog_dct.keys(), reverse=True)])





'''
1.  Напишите программу вычисления арифметического выражения заданного строкой.
    Используйте операции +,-,/,*. приоритет операций стандартный.
        Пример:
        2+2 => 4;
        1+2*3 => 7;
        1-2*3 => -5;
'''
# ------------< Решения 1 >-------------

# s = '10*55+21*2'

# lst = []
# last = -1
# for i in range(len(s)):
#     if s[i] in {'+', '-', '*', '/'}:
#         lst.append(s[last + 1:i])
#         lst.append(s[i])
#         last = i
# lst.append(s[last + 1])
# print(lst)

# s = lst

# lst_res = [int(s[0])]
# i = 1
# while i < len(s):
#     if s[i] == '+':
#         lst_res.append(int(s[i + 1]))
#     elif s[i] == '-':
#         lst_res.append(-int(s[i + 1]))
#     elif s[i] == '*':
#         lst_res[-1] *= int(s[i + 1])
#     elif s[i] == '/':
#         lst_res[-1] /= int(s[i + 1])
#     i += 2

# print(lst_res)
# print(sum(lst_res))



# ------------< Решения 2 >-------------

# def get_dict_from_polinom(str_pol):
#     lst = []
#     last_index = -1
#     neg = False
#     for i, char in enumerate(str_pol):
#         if char == '+' or char == '-':
#             if neg:
#                 lst.append('-' + str_pol[last_index + 1:i])
#             else:
#                 lst.append(str_pol[last_index + 1:i])
#             last_index = i
#             neg = char == '-'
#     if neg:
#         lst.append('-' + str_pol[last_index + 1:])
#     else:
#         lst.append(str_pol[last_index + 1:])
#     return lst

# lst = get_dict_from_polinom("1-22*33")
# print(lst)
# sums_2 = 0
# for i in lst:
#     if "*" in i or "/" in i:
#         prods = i.split("*")
#         prod = 1
#         for char in prods:
#             if "/" in char:
#                 dels = char.split("/")
#                 r = int(dels[0])
#                 for k in range(1, len(dels)):
#                     r /= int(dels[k])
#             else:
#                 r = int(char)
#             prod *= r
#         sums_2 += prod
#     else:
#         sums_2 += int(i)
# print(sums_2)





'''
2 Добавьте возможность использования скобок, меняющих приоритет операций.
        Пример:
        1+2*3 => 7;
        (1+2)*3 => 9;
'''

# ------------< Решения 1 >-------------

# operation = "(2+2)*(2+4)+44/2"
# operation = operation.replace(" ", "")
 
 
# def minus(lst):
#     return lst[0] - lst[1]
 
 
# def multi(lst):
#     return lst[0] * lst[1]
 
 
# def divide(lst):
#     return lst[0] / lst[1]
 
 
# def count_from_string(operation):
#     if "(" in operation:
#         bk1 = operation.rindex("(")
#         bk2 = operation.index(")", bk1)
#         return count_from_string(operation[:bk1] + str(count_from_string(operation[bk1 + 1:bk2])) + operation[bk2 + 1:])
#     if operation.isdigit():
#         return int(operation)
#     if "+" in operation:
#         return sum([count_from_string(item) for item in operation.split("+", 1)])
#     if "-" in operation:
#         return minus([count_from_string(item) for item in operation.split("-", 1)])
#     if "/" in operation:
#         return divide([count_from_string(item) for item in operation.split("/", 1)])
#     if "*" in operation:
#         return multi([count_from_string(item) for item in operation.split("*", 1)])
 
 
# print(count_from_string(operation))




'''
3.  Дана последовательность чисел. 
    Получить список уникальных элементов заданной последовательности.

        [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
'''

















