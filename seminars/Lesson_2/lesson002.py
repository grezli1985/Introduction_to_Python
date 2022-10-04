''' 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    - Для N = 5: 1, -3, 9, -27, 81 '''

# n = int(input())
# a = 1
# for i in range(n):
#     a *= -3
#     # a=(-3)**i
#     print(a, end=' ')

# def show_sequence(n):
#     for i in range(n):
#         num = (-3)**i
#         print(num, end=' ')


# num = int(input("Введите целое число: "))
# show_sequence(num)



''' 2. Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
    - Для n = 6: [4, 7, 10, 13, 16, 19] '''

def N_sequence(N):
    pos = []
    i = 1
    while (i <= N):
        pos.append(3 * i + 1)
        i += 1
    return pos

# print(N_sequence)


n = int(input())
res = []
for i in range(1, n + 1):
    res.append(3 * i + 1)
print(res)



''' 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество
   вхождений одной строки в другой.

   ssabababsdaasd aba -> 2 '''

a = "aaaaaaaaababasss"
b = "aba"
length = len(a) - len(b)
count = 0
for i in range(length + 1):
    if b in a[i:i + len(b)]:
        count += 1
print(count)


def f(a, b):
    count = 0
    for i in range(len(a) - len(b)):
        print('->>', a[i:i + len(b)])
        if b == a[i:i + len(b)]:
            count += 1
    return count