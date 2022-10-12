# import random

# # random.seed(55)

# print(random.randint(0, 100))
# print(random.randint(0, 100))
# print(random.randint(0, 100))




# n = 10
# fib = [0, 1]

# for i in range(n - 1):
#     fib.append(fib[-2] - fib[-1])

# fib.reverse()

# for i in range(n):
#     fib.append(fib[-1] + fib[-2])

# print(fib)









# with open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_4/new_file',
#         'r', encoding='utf-8') as f:     # rt - текстовый, rb - бинарный, w - открытия на запись с перезаписью, a - открытия на запись с дополнением 
#     print(1, f.readline())
#     print(2, f.readlines())

# f.close()


# from time import sleep

# with open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_4/new_file',
#         'r', encoding='utf-8') as f:
#     while True:
#         sleep(2)
#         print(next(f))




# with open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_4/new_file',
#         'r', encoding='utf-8') as f:
#     lines = f.readlines()


# print(lines)
# print(lines)
# print(lines)






# with open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_4/new_file',
#         'r', encoding='utf-8') as f:
#     lines = f.readlines()

# print(lines)
# lines[3] = 'Hello!!!\n'

# with open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_4/new_file',
#         'w', encoding='utf-8') as f:
#     for line in lines:
#         f.write(line)







# фактариал

# # 4!
# # 3! * 4
# # 2! * 3 * 4
# # 1! * 2 * 3 * 4
# # 1 * 2 * 3 * 4

# def fact(n):
#     if n < 0:
#         return
#     elif n == 1:
#         return 1
#     return fact(n - 1) * n

# print(fact(5))              # 120









# фибоначчи



# def fib(n):
#     if n <= 2:
#         return 1
    
#     return fib(n - 1) + fib(n - 2)

# print(fib(25))            # Если брать большое значения будем ждать очень долго
                            # дерево параллельных расчетов очень тормазит систему





# mem = {1: 1, 2: 1}

# def fib(n):
#     if n not in mem:                         # Если n я не разу не считал
#         mem[n] = fib(n - 1) + fib(n - 2)     # То я его выщетаю (всего один раз, и и сохраню в словарь )
#     return mem[n]                            # (кеширования)Мы каждый вызов сохраняем в словарь и больше его не используем

# print(fib(405))





'''
1. Задайте строку из набора чисел. Напишите программу,
   которая покажет большее и меньшее число.
   В качестве символа-разделителя используйте пробел.
'''

# nums = list(map(int, input().split()))
# nums.sort()
# print(nums[0], nums[- 1]) 



'''
2. Найдите корни квадратного уравнения Ax² + Bx + C = 0
с помощью математических формул нахождения корней квадратного уравнения
'''

# a, b, c = list(map(int, input().split()))

# if a != 0 and (b**2 - 4 * a * c) >= 0:
#     x1 = (- b - (b**2 - 4 * a * c)**0.5) / (2 * a)
#     x2 = (- b + (b**2 - 4 * a * c)**0.5) / (2 * a)
#     print({x1, x2})
# else:
#     print('Корней нет!')




'''
3. Задайте два числа. Напишите программу, которая найдёт НОК 
   (наименьшее общее кратное) этих двух чисел.
'''

# a, b = list(map(int, input().split()))

# for i in range(min(a, b) + 1, 1, -1):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break
# else:
#     print('нет общего делителя')



# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = num1
# num4 = num2

# while num1 != 0 and num2 != 0:
#     if num1 > num2:
#         num1 = num1 % num2
#     else:
#         num2 = num2 % num1
# gcd = num1 + num2
# print(abs(num3 * num4) / gcd)





