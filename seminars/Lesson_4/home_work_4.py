from random import*
from math import pi

''' 
    1 Вычислить число π c заданной точностью d

        Пример:

        - при $ d = 0.001, π = 3.141. $    $ 10^{-1} ≤ d ≤10^{-10} $

    π = 2√3*(1 - (1/3)*(1/3) + (1/5)*(1/3)^2 - (1/7)*(1/3)^3
    p = 2 ** 3 *(1 - (1/3) * (1/3) + (1/5) * (1/3) ** 2 - (1/7) * (1/3) ** 3
    π = 2√3*(1 - (1/3)*(1/3) + (1/5)*(1/3)^2 - (1/7)*(1/3)^3… + 1/((2n + 1)*(-3)^n)…)

    https://completerepair.ru/kak-vychislit-chislo-pi         
'''


# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# d = int(input('Введите число: '))
# # π = 3,1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989
# # print(π)
# # if 10**{-1} <= d <= 10**{-10}:
# for n in range(1, d):
#     π = (2 ** 3 * 1 - (1/3) * (1/3) + (1/5) * (1/3) ** 2 - (1/7) * (1/3) ** 3)/4
#         # (4/n) - (4/n) + (4/n) - (4/n) + (4/n) - (4/n) + (4/n) - (4/n) + (4/n)
# print(round(π, d))

# d =  int(input("Введите число для заданной точности числа Пи:\n"))

# def calc_pi(eps=1.0e-5):
#     s = 0
#     d = 1
#     sgn = 1
#     while True:
#         a = 4 / d
#         s = s + sgn * a
#         if a < eps:
#             return s
#         sgn = -sgn
#         d += 2
 
# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# pi = calc_pi
# p = round(pi, d)
# print(p)


''' 
    2 Задайте натуральное число N. Напишите программу, 
    которая составит список простых множителей числа N.

        Пример:

            - при N=236     ->        [2, 2, 59]     
'''


# n = int(input("Введите натуральное число N: "))

# def prime_factors_number(n):
#     result = []

#     for i in range(2, n + 1):
#         while n % i == 0:
#             n /= i
#             result.append(i)
#     return result

# print(f"Результат: {prime_factors_number(n)}")



''' 
    3 Задайте последовательность чисел.
    Напишите программу, которая выведет список неповторяющихся 
    элементов исходной последовательности.

        Пример:

    - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]   
'''

# a = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]

# print([i for i in a if a.count(i) == 1])


''' 
    4 Задана натуральная степень k. 
    Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
    многочлена и записать в файл многочлен степени k.

        Пример: 

        - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0         
'''

# def write_file(st):
#     path = "/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_4/polynomial_file"
#     with open(path, 'w') as data:
#         data.write(st)

# k = int(input("Введите натуральную степень k = "))
# polynomial = list()

# while k >= 0:
#     num = randint(0, 101)
#     if num == 0 and k == 0: 
#         s=('= 0')
#     elif num == 0:
#         k -= 1
#         continue
#     if k == 0:
#         polynomial.append(str(num))
#         # print(f'{num} = 0')
#     elif k == 1:
#         polynomial.append(str(num) + "x")
#         # print(f'{num} * x + ', end = '')
#     else:
#         polynomial.append(str(num) + ' * ' + "x ** " + str(k))
#         # print(f'{num} * x ** {k} + ', end = '')
#     k -= 1

# s = " + ".join(polynomial) + " = 0"
# print(s)

# write_file(s)





'''
    5 Даны два файла, в каждом из которых находится запись многочлена. 
    Задача - сформировать файл, содержащий сумму многочленов.
    Коэффициенты могут быть как положительными, так и отрицательными. 
    Степени многочленов могут отличаться. 

    
    
    
    5x^2 + 3x - 9
    3x^2 - 2x - 5

    8x^2 + 1x - 14    
'''

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


#     # return dct        


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

