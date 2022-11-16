from datetime import datetime
import telebot
import csv
import math, cmath
from telebot import TeleBot, types


bot = TeleBot('5612294742:AAGJqESZ2PLT-4_AWA_hyDzUhZas8wCwFvU')
dict = {"Фамилия": None, "Имя": None, "Телефон": None, "Описание": None}
value = ''
old_value = ''


def logger_action(action: str):
    with open('log.txt', 'a', encoding='utf-8') as data:
        data.write(f'{datetime.now().strftime("%Y-%m-%d-(%H) %H:%M")} Пользователь {action} \n')


keyboard = types.InlineKeyboardMarkup()
keyboard.row(   types.InlineKeyboardButton('j', callback_data='j'),
                types.InlineKeyboardButton('C', callback_data='c'),
                types.InlineKeyboardButton('<=', callback_data='<='),
                types.InlineKeyboardButton('Pi', callback_data='pi'))

keyboard.row(   types.InlineKeyboardButton('%', callback_data='%'),
                types.InlineKeyboardButton('1/x', callback_data='1/x'),
                types.InlineKeyboardButton('x^2', callback_data='x^2'),
                types.InlineKeyboardButton('√', callback_data='2^x'))

keyboard.row(   types.InlineKeyboardButton('sin', callback_data='sin'),
                types.InlineKeyboardButton('cos', callback_data='cos'),
                types.InlineKeyboardButton('tg', callback_data='tan'),
                types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(   types.InlineKeyboardButton('7', callback_data='7'),
                types.InlineKeyboardButton('8', callback_data='8'),
                types.InlineKeyboardButton('9', callback_data='9'),
                types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(   types.InlineKeyboardButton('4', callback_data='4'),
                types.InlineKeyboardButton('5', callback_data='5'),
                types.InlineKeyboardButton('6', callback_data='6'),
                types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(   types.InlineKeyboardButton('1', callback_data='1'),
                types.InlineKeyboardButton('2', callback_data='2'),
                types.InlineKeyboardButton('3', callback_data='3'),
                types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(   types.InlineKeyboardButton('+/-', callback_data='+/-'),
                types.InlineKeyboardButton('0', callback_data='0'),
                types.InlineKeyboardButton(',', callback_data='.'),
                types.InlineKeyboardButton('=', callback_data='='))

keyboard.row(   types.InlineKeyboardButton('(', callback_data='('),
                types.InlineKeyboardButton(')', callback_data=')'))

@bot.message_handler(commands=['calculator'])
def start_calculater(msg: telebot.types.Message):
    logger_action('запустил калькулятор.')
    global value
    if value == '':
        bot.send_message(msg.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(msg.from_user.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_function(query):
    global value, old_value
    data = query.data

    logger_action(f'внес данные: {data} .')
    if data == 'c':
        if old_value != '':
            value = ''
        else:
            pass
    elif data == '%':
        if value != '':
            try:
                value = str((eval(value) / 100))
            except:
                value = 'Error'
        else:
            pass
    elif data == 'sin':
        if value != '':
            try:
                value = str(math.sin(eval(value)))
            except:
                try:
                    value = str(cmath.sin(eval(value)))
                except:
                    value = 'Error'
        else:
            value = str(math.sin(0))
        logger_action(f'получил значение {value}')
    elif data == 'cos':
        if value != '':
            try:
                value = str(math.cos(eval(value)))
            except:
                try:
                    value = str(cmath.cos(eval(value)))
                except:
                    value = 'Error'
        else:
            value = str(math.cos(0))
        logger_action(f'получил значение {value}')
    elif data == 'tan':
        if value != '':
            try:
                value = str(math.tan(eval(value)))
            except:
                try:
                    value = str(cmath.tan(eval(value)))
                except:
                    value = 'Error'
        else:
            value = str(math.tan(0))
        logger_action(f'получил значение {value}')
    elif data == 'pi':
        value += str(math.pi)
    elif data == '1/x':
        if value != '':
            try:
                value = str(1 / (eval(value)))
            except:
                value = 'Error'
            logger_action(f'получил значение {value}')
        else:
            pass
    elif data == 'x^2':
        if value != '':
            try:
                value = str(pow(eval(value), 2))
            except:
                value = 'Error'
            logger_action(f'получил значение {value}')
        else:
            pass
    elif data == '2^x':
        if value != '':
            try:
                if value.count('j'):
                    value = str(cmath.sqrt(eval(value)))
                else:
                    value = str(math.sqrt(eval(value)))
            except:
                value = 'Error'
            logger_action(f'получил значение {value}')
        else:
            pass
    elif data == '=':
        try:
            if value.count('j'):
                logger_action('производит расчеты с комплексными числами.')
            logger_action(f'ввел пример: {value}')
            value = str(eval(value))
            logger_action(f'получил значение: {value} .')
        except Exception:
            value = 'Error'
            logger_action(f'получил ошибку вычисления.')
    elif data == '<=':
        if value != '':
            value = value[:-1]
            logger_action(f'получил значение {value}')
        else:
            pass
    elif data == '+/-':
        try:
            value = str( eval(value) * -1 )
        except:
            value = 'Error'
        logger_action(f'получил значение {value}')
    elif data == '0':
        try:
            if old_value != '0':
                value += data
            else:
                raise Exception
        except Exception:
            value = 'Error'
    elif data == 'j':
        if value[-1] != 'j':
            value += data
        else:
            pass
    else:
        if (value == '0' and not data.isdigit()) or value != '0':
            value += data
        elif value == '0' and data.isdigit():
            value += data
            value = value[1:]
    try:
        if (value != old_value and value != '') \
            or (old_value != '0' and value == ''):
            if value == '':
                bot.edit_message_text(\
                    chat_id=query.message.chat.id,\
                        message_id=query.message.message_id,\
                            text='0',\
                                reply_markup=keyboard)
                old_value = '0'
            else:
                bot.edit_message_text(\
                    chat_id=query.message.chat.id,\
                        message_id=query.message.message_id,\
                            text=value, reply_markup=keyboard)
                old_value = value
        else:
            raise Exception
    except Exception:
        value = 'Error'
    old_value = value

    if value == 'Error':
        logger_action('получил ошибку ввода')
        value = ''


@bot.message_handler(commands=['get_file'])
def ge_file(msg: telebot.types.Message):
    logger_action('открыл фаил TestBot.log.')
    bot.send_message(chat_id=msg.from_user.id, text='Споем вместе\nYPA!!! открывай меня')
    bot.send_document(chat_id=msg.from_user.id, document=open('TestBot.log', 'rb'))


@bot.message_handler(content_types=['document'])
def hello_document(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(msg.document.file_name, 'wb') as f_out:
        f_out.write(downloaded_file)
    logger_action(f'{msg.from_user} загрузил документ: {msg.document.file_name}.')


@bot.message_handler(commands=['start'])
def start(msg: telebot.types.Message):
    logger_action('Бот запущен.')
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
    if msg.chat.type == 'private':
        if msg.text == 'справка':
            logger_action('посмотрел справку.')
            bot.send_message(msg.chat.id, 'Есть команды\n/start\n/calculator\n/get_file')
        elif msg.text == 'документ':
            logger_action('документ')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itemp1 = types.KeyboardButton('открыть')
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
            itemp2 = types.KeyboardButton('стикер')
            back = types.KeyboardButton('назад')        
            markup.add(itemp1, itemp2, back)

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
            logger_action('назад')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            itemp1 = types.KeyboardButton('справка')
            itemp2 = types.KeyboardButton('документ')
            itemp3 = types.KeyboardButton('крестики нолики')
            itemp4 = types.KeyboardButton('калькулятор')
            itemp5 = types.KeyboardButton('Телефонная книга')
    
            markup.add(itemp1, itemp2, itemp3, itemp4, itemp5)
        
            bot.send_message(msg.chat.id, 'назад', reply_markup = markup)    

        elif msg.text == 'открыть':
            ge_file(msg)

        elif msg.text == 'стикер':
            logger_action('посмотрел стикер.')
            stick = open('obnimash.webp', 'rb')
            bot.send_sticker(msg.chat.id, stick)

        elif msg.text == 'Просмотр записей':
            logger_action('посмотрел запись.')
            bot.send_document(msg.chat.id, document=open('book.csv', 'rb'))    
        
        elif msg.text == 'Добавление записи':
            logger_action('Добавление записи.')
            next_message = bot.send_message(chat_id=msg.from_user.id, text=f"Введите фамилию:")
            bot.register_next_step_handler(callback=input_surname, message=next_message)            

        elif msg.text == 'Экспорт':
            bot.send_document(chat_id=msg.from_user.id, document=open('log.txt', 'rb'))
            
        elif msg.text == 'Импорт':
            bot.send_message(chat_id=msg.from_user.id, text=f"прикрепи фаил")


def input_surname(msg):
    global dict
    dict["Фамилия"] = msg.text.capitalize()
    next_message = bot.send_message(chat_id=msg.from_user.id, text="Введите имя:")
    bot.register_next_step_handler(callback=input_name, message=next_message)

def input_name(msg):
    global dict
    dict["Имя"] = msg.text.capitalize()
    next_message = bot.send_message(chat_id=msg.from_user.id, text="Введите телефон:")
    bot.register_next_step_handler(callback=input_tel, message=next_message)

def input_tel(msg):
    global dict
    tel = check_tel(msg.text)
    if tel:
        dict["Телефон"] = tel
        next_message = bot.send_message(chat_id=msg.from_user.id, text="Введите описание:")
        bot.register_next_step_handler(callback=input_discription, message=next_message)
    else:
        next_message = bot.send_message(chat_id=msg.from_user.id, text="Введён некорректный телефон\nВведите телефон:")
        bot.register_next_step_handler(callback=input_tel, message=next_message)

def input_discription(msg):
    global dict
    dict["Описание"] = msg.text
    add_note(dict["Фамилия"], dict["Имя"], dict["Телефон"], dict["Описание"])
    bot.send_message(chat_id=msg.from_user.id, text=f"Данные внесены")

def check_tel(s):
    if s.isdigit() and len(s) == 11:
        l = [i for i in s]
        edit_tel = ["+7"] + ["("] + l[1:4] + [")"] + l[4:7] + ["-"] + l[7:9] + ["-"] + l[9:]
        return "".join(edit_tel)

    elif s.isdigit() and len(s) == 7:
        l = [i for i in s]
        edit_tel = l[0:4] + ["-"] + l[4:6] + ["-"] + l[6:]
        return "".join(edit_tel)

    elif s.isdigit():
        return s

    else:
        return False

def add_note(family=None, name=None, tel=None, discription=None):   
    with open("book.csv", "a", newline="") as file:
        fieldnames = ["Фамилия", "Имя", "Телефон", "Описание"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"Фамилия": family, "Имя": name, "Телефон": tel, "Описание": discription})
        

@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f"Вы ввели: {msg.text}")

bot.polling(none_stop= True)