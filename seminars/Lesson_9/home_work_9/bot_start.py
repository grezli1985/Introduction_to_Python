import telebot
from telebot import TeleBot, types
# from xml.dom.minidom import Document
from datetime import datetime as dt
from math import sqrt
import cmath

bot = TeleBot('5612294742:AAGJqESZ2PLT-4_AWA_hyDzUhZas8wCwFvU')

with open('log.txt', 'a') as f_log:
    print(dt.now(), 'Бот запущен', file=f_log)

def logs(msg: telebot.types.Message):
    with open("log.txt", "a") as f_log:
        print(dt.now(), f'Пользователь ({msg.from_user.id}) прислал сообщение: {msg.text}', file=f_log)    

value = ''
old_value = ''

Keyboard = telebot.types.InlineKeyboardMarkup()
Keyboard.row(   telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('C', callback_data='C'),
                telebot.types.InlineKeyboardButton('<=', callback_data='<='),
                telebot.types.InlineKeyboardButton('/', callback_data='/'))

Keyboard.row(   telebot.types.InlineKeyboardButton('7', callback_data='7'),
                telebot.types.InlineKeyboardButton('8', callback_data='8'),
                telebot.types.InlineKeyboardButton('9', callback_data='9'),
                telebot.types.InlineKeyboardButton('*', callback_data='*'))

Keyboard.row(   telebot.types.InlineKeyboardButton('4', callback_data='4'),
                telebot.types.InlineKeyboardButton('5', callback_data='5'),
                telebot.types.InlineKeyboardButton('6', callback_data='6'),
                telebot.types.InlineKeyboardButton('-', callback_data='-'))

Keyboard.row(   telebot.types.InlineKeyboardButton('1', callback_data='1'),
                telebot.types.InlineKeyboardButton('2', callback_data='2'),
                telebot.types.InlineKeyboardButton('3', callback_data='3'),
                telebot.types.InlineKeyboardButton('+', callback_data='+'))

Keyboard.row(   telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('0', callback_data='0'),
                telebot.types.InlineKeyboardButton(',', callback_data='.'),
                telebot.types.InlineKeyboardButton('=', callback_data='='))

@bot.message_handler(commands=['calculator'])
def start_calculater(msg: telebot.types.Message):
    logs(msg)
    global value
    if value == '':
        bot.send_message(msg.from_user.id, '0', reply_markup=Keyboard)
    else:
        bot.send_message(msg.from_user.id, value, reply_markup=Keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[len(value)-1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Ошибка!'
    else:
        value += data

    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=Keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=Keyboard)
            old_value = value

    
    if value == 'Ошибка!':
        value = ''


def csolve(text):
    a, b, c = text
    d = b**2 - 4*a*c
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    return (x1, x2)


def sum_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=csolve(msg.text))


# @bot.message_handler(commands=['games'])
# def games(msg: telebot.types.Message):
#     bot.send_game(chat_id=msg.from_user.id, game_short_name='крестики нолики')

@bot.message_handler(commands=['get_file'])
def ge_file(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Споем вместе\nYPA!!! открывай меня')
    bot.send_document(chat_id=msg.from_user.id, document=open('TestBot.log', 'rb'))


@bot.message_handler(commands=['get_record'])
def record(msg: telebot.types.Message):
    logs(msg)
    # input_data(msg)
    with open('book.txt', 'a+', encoding='utf-8') as data:
        print(f'{msg.text}', file=data)
    

@bot.message_handler(content_types=['document'])
def document(msg: telebot.types.Message):
    logs(msg)
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(msg.document.file_name, 'wb') as f_out:
        f_out.write(downloaded_file)


@bot.message_handler(commands=['start'])
def start(msg: telebot.types.Message):
    logs(msg)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itemp1 = types.KeyboardButton('справка')
    itemp2 = types.KeyboardButton('документ')
    itemp3 = types.KeyboardButton('крестики нолики')
    itemp4 = types.KeyboardButton('калькулятор')
    itemp5 = types.KeyboardButton('Телефонная книга')

    markup.add(itemp1, itemp2, itemp3, itemp4, itemp5)
    
    bot.send_message(msg.chat.id, 'Привет, {0.first_name}!'.format(msg.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(msg: telebot.types.Message):
    logs(msg)
    if msg.chat.type == 'private':
        if msg.text == 'справка':
            bot.send_message(msg.chat.id, 'Есть команды\n/start\n/calculator\n/get_file')
        elif msg.text == 'документ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itemp1 = types.KeyboardButton('открыть')
            bot.register_next_step_handler(msg, ge_file)
            itemp2 = types.KeyboardButton('???? ????')
            back = types.KeyboardButton('назад')        
            markup.add(itemp1, itemp2, back)

            bot.send_message(msg.chat.id, 'документ', reply_markup = markup)
            
        
        elif msg.text == 'крестики нолики':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itemp1 = types.KeyboardButton('X')
            itemp2 = types.KeyboardButton('O')
            back = types.KeyboardButton('назад')        
            markup.add(itemp1, itemp2, back)

            bot.send_message(msg.chat.id, 'крестики нолики', reply_markup = markup)

        elif msg.text == 'калькулятор':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itemp1 = types.KeyboardButton('/calculator')
            itemp2 = types.KeyboardButton('комплексные')
            itemp3 = types.KeyboardButton('стикер')
            back = types.KeyboardButton('назад')        
            markup.add(itemp1, itemp2, itemp3, back)

            bot.send_message(msg.chat.id, 'калькулятор', reply_markup = markup)

        elif msg.text == 'Телефонная книга':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itemp1 = types.KeyboardButton('Просмотр записей')
            itemp2 = types.KeyboardButton('Добавление записи')
            itemp3 = types.KeyboardButton('Экспорт')
            itemp4 = types.KeyboardButton('Импорт')
            back = types.KeyboardButton('назад')        
            markup.add(itemp1, itemp2, itemp3, itemp4, back)

            bot.send_message(msg.chat.id, 'Телефонная книга', reply_markup = markup)

        elif msg.text == 'назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itemp1 = types.KeyboardButton('справка')
            itemp2 = types.KeyboardButton('документ')
            itemp3 = types.KeyboardButton('крестики нолики')
            itemp4 = types.KeyboardButton('калькулятор')
            itemp5 = types.KeyboardButton('Телефонная книга')
    
            markup.add(itemp1, itemp2, itemp3, itemp4, itemp5)
        
            bot.send_message(msg.chat.id, 'назад', reply_markup = markup)    

        elif msg.text == 'комплексные':
            logs(msg)
            bot.send_message(chat_id=msg.from_user.id, text="Введите цифры: ")
            bot.register_next_step_handler(callback=sum_items, message=msg)

        elif msg.text == 'стикер':
            logs(msg)
            stick = open('обнимашки.webp', 'rb')
            bot.send_sticker(msg.chat.id, stick)

        elif msg.text == 'Просмотр записей':
            # logs(msg)
            bot.send_document(msg.chat.id, document=open('book.txt', 'rb'))    
        
        elif msg.text == 'Добавление записи':    
            bot.send_message(chat_id=msg.from_user.id, text='Введите ФИО: ')
            bot.send_message(chat_id=msg.from_user.id, text='Введите телефон: ')
            bot.send_message(chat_id=msg.from_user.id, text='Введите примечание: ')
            bot.register_next_step_handler(msg, record)
            

        elif msg.text == 'Экспорт':
            bot.send_document(chat_id=msg.from_user.id, document=open('log.txt', 'rb'))
            
        elif msg.text == 'Импорт':
            bot.send_message(chat_id=msg.from_user.id, text=f"прикрепи фаил")


@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f"Вы ввели: {msg.text}")

bot.polling(none_stop= True)

