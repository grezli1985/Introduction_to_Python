'''1. Напишите программу, которая принимает на вход два числа и 
      проверяет, является ли одно число квадратом другого.
    
    *Примеры:* 
    
    - 5, 25 -> да
    - 4, 16 -> да
    - 25, 5 -> да
    - 8, 9 -> нет'''


# a = int(input('Введите a: '))
      
# b = int(input('Введите b: '))

# def square_another(a, b):
#     if a/b==b:
#         print('да')
#     elif b/a==a:
#         print('да')
#     else:
#         print('нет')


# square_another(a, b)

'''2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
    Примеры:
    
    - 1, 4, 8, 7, 5 -> 8
    - 78, 55, 36, 90, 2 -> 90'''

# def large(lst):
#     max_ = lst[0]
#     for i in lst:
#         if i > max_:
#             max_ = i
#     return max_


# lst = [1, 2, 3, 4, 5]
# result = large(lst)
# print(result)





'''3. Программа получает на вход число. 
        Необходимо вывести список простых множителей этого числа.
        
        236 -> 2, 2, 59  -> 2 * 2 * 59 = 236'''

a = int(input("Введите число: "))
result = []
temp_a = a

for i in range(2, a):
    while temp_a % i == 0:
        result.append(i)
        temp_a = temp_a // i

print(result)



k = 2
numbs = []
a = int(input('Введите число : '))
while a != 1:
    if a % k == 0:
        numbs.append(k)
        a //= k
    else:
        k += 1
print(numbs)


