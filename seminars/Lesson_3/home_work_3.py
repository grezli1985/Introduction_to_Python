''' Задача 1
    Задайте список из нескольких чисел. Напишите программу,
    которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 '''



# a = [2, 3, 5, 9, 3]
# sum_ = 0;
# for i in range(len(a)):
#     if i % 2 == 1:
#         sum_ += a[i];
# print(sum_)

 

''' Задача 2
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]  '''


# a = [2, 3, 5, 6] 
# # a = [2, 3, 4, 5, 6]

# if len(a) % 2 != 0:
#     length = int(len(a) / 2) + 1
# else:
#     length = int(len(a) / 2)

# for i in range(0, length):
#     print(a[i] * a[len(a) - 1 - i])
       


''' Задача 3
Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и
минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19   '''


# a = [1.1, 1.2, 3.1, 5, 10.01]

numbers = [1.1, 1.2, 3.1, 5, 10.01]

def only_decimal(list):
    decimal = []
    for i in range(0, len(list)):
        if list[i] % 1 != 0:
            decimal.append(round(list[i] % 1, 2))
    return decimal
    
def diff(list):
    for i in range(0, len(list)):
        diff = max(list) - min(list)
    return diff

decimal = (only_decimal(numbers))
print(diff(decimal))

''' Задача 4
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10   '''


# number = int(input("Введите число = "))
# result = 0
# bi = 1

# while number > 0:
#     result += number % 2 * bi
#     bi *= 10
#     number //= 2
    
# print(result)



''' Задача 5
Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
Негафибоначчи  '''

# def fib(n):
#     if n  in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 11):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21

# def fibo(n):
#     if n >= 0:
#         idx = range(n + 1)
#         x = [0, 1]
#         for k in idx[2:]:
#             x.append(x[k - 1] + x[k - 2]) 
#         return x[n]
#     else:
#         n = -(n - 1)
#         idx = range(n + 1)
#         x = [1, 0]
#         for k in idx[2:]:
#            x.append(x[k - 2] - x[k - 1]) 
#         x.reverse()
#     return x[0]

# for i in range(-8, 9):
#     print(fibo(i), end= ' ')
