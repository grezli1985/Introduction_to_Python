'''
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''


# path = "/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_5/2_file"
# with open(path, 'w', encoding="UTF-8") as data:
#     data.write('1 abc 2 3 4 6 abc 5 7 8 abc9')

# with open(path, "r", encoding="UTF-8") as data:
#     string = data.readline().split()
# result = list(filter(lambda x: 'abc' not in x, string))
# print(string)
# print(result)





# txt = '1 abc 2 3 4 6 abc 5 7 8 abc9'
# find_txt = "abc"
# print([i for i in txt.split() if find_txt not in i])





'''
2. Создайте программу для игры с конфетами человек против человека.

    Условие задачи: На столе лежит 2021 конфета. 
    Играют два игрока делая ход друг после друга. 
    Первый ход определяется жеребьёвкой. 
    За один ход можно забрать не более чем 28 конфет. 
    Все конфеты оппонента достаются сделавшему последний ход. 
    Сколько конфет нужно взять первому игроку, 
    чтобы забрать все конфеты у своего конкурента?

    a) Добавьте игру против бота

    b) Подумайте как наделить бота ""интеллектом""
'''


# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")




'''
3. Создайте программу для игры в ""Крестики-нолики"".

  0 |   | x
--------------       
  0 | x | 
--------------      
  x |   |     
'''


# print('*' * 15, '  <<<<< Крестики - нолики >>>>>  ', '*' * 15)

# board = list(range(1, 10))

# def draw_board(board):     # создает поле
#     print('-' * 13)
#     for i in range(3):
#         print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
#         print('-' * 13)

# def take_input(player_token):     # Собирает всю инфу от пользователя и проверяет
#     valid = False
#     while not valid:
#         player_answer = input('Куда поставим: ' + player_token + '? ')

#         try:
#             player_answer = int(player_answer)
#         except:
#             print('Некорректный ввод. Вы уверены, что ввели число?')
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if(str(board[player_answer - 1]) not in 'XO'):
#                 board[player_answer - 1] = player_token
#                 valid = True
#             else:
#                 print('Эта клетка уже занята!')
#         else:
#             print('Введите число от 1 до 9')

# def check_win(board):  # вареантты выигрыша
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6),)
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):             #  сбор 
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input('Х')
#         else:
#             take_input('О')
#         counter += 1

#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, 'Ты выиграл!')
#                 win = True
#                 break
#         if counter == 9:
#             print('Ничья!')
#             break
#     draw_board(board)

# main(board)





'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


aaaaaaaaaaaaaaaaaaaaaaabbb222aaabbwwwwcc
9a9a5a3323a2b4w2c

'''


# data = 'aaaaaaaaaaaaaaaaaaaaaaabbb222aaabbwwwwcc'

# def rle(data):
#     prev = ''
#     lst = ''
#     count = 1
#     for item in data:
#         if item != lst:
#             if lst:
#                 prev += str(count) + lst
#             lst = item
#             count = 1
#         else:
#             count += 1
#     else:
#         prev += str(count) + lst
#         return prev


# print(rle(data))
        
    



'''
5*. Дан список чисел. Создайте список, в который попадают числа,
описываемые возрастающую последовательность. Порядок элементов менять нельзя.
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

Входные и выходные данные хранятся в отдельных текстовых файлах.
'''
# itog = set()

# def f(lst, cur=None, i=0):
#     cur = [] if cur is None else cur
#     if i == len(lst):
#         if len(cur) > 1:    
#           itog.add(tuple(cur))
#         return
#     f(lst, cur, i + 1)
#     for index in range(i, len(lst)):
#         if cur and cur[-1] < lst[index]:
#             f(lst, cur + [lst[index]], index + 1)
#         elif not cur:
#               f(lst, [lst[index]], index + 1)

# f([1, 5, 2, 3, 4, 6, 1, 7])
# print(len(itog))
# print(max(itog, key=lambda x: len(x)))
# # print(*sorted(itog), sep='\n')
