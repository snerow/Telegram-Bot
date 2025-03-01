# НЕ ДЛЯ ИСПОЛЬЗОВАНИЯ

# Файл, где хранятся нереализованные/удалённые функции программы

import telebot
from telebot import types


# объект бота с токеном из @BotFather в телеге
bot = telebot.TeleBot('7322799513:AAFErWKfIx-dKUFzuk7aLNJKsE2YIiRYBqE')


# обработка команд /site и /website, которые перекидывают пользователя на оф. сайт ТС
@bot.message_handler(commands=['site', 'website'])
def site(message):
    bot.send_message(message.chat.id, url='https://tstroy33.ru')


# команда /run, которая запускает логику расчёта стоимости дымохода
@bot.message_handler(commands=['run'])
def run(message):
    a = 0