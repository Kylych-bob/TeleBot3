import telebot
import xmlto

# from telebot import types

x = xmlto.main()
# print(x['date'])


bot = telebot.TeleBot('1293520916:AAFTppG4ngUsF7YMkmpLyI8KrdKh39CvwZM')
# @bot.message_handler(commands=['start', 'старт'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Hello! How are you?')


convert = None
@bot.message_handler(commands=['start', 'старт'])
def start_message(message):
    bot.send_message(message.chat.id, f"Здравствуйте курсы на сегодня: {x['date']}\n USD = {x['USD']} \n EUR = {x['EUR']} \n KZT = {x['KZT']}\n RUB = {x['RUB']}")
    bot.send_message(message.chat.id, 'На какую валюту хотите сконвертировать сом: \n 1 - USD \n 2 - EUR \n 3 - KZT \n 4 - RUB')

@bot.message_handler(content_types=['text'])
def converting(message):
    global convert
    if message.text == '1':
        convert = x['USD'].replace(",",".")
    elif message.text == '2':
        convert = x['EUR'].replace(",",".")
    elif message.text == '3':
        convert = x['KZT'].replace(",",".")
    elif message.text == '4':
        convert = x['RUB'].replace(",",".")
        # return convert 
    convert = float(convert) 
    print(convert)
    message = bot.send_message(message.chat.id,"Введите количество сомов:")
    bot.register_next_step_handler(message, get_soms)


def get_soms(message):
    soms = float(message.text)
    result = soms / convert
    print(convert)
    bot.send_message(message.chat.id,f"Ваш {soms} равен {result}")
    


bot.polling()