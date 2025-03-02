# НЕ ДЛЯ ИСПОЛЬЗОВАНИЯ

# Файл, где хранятся нереализованные/удалённые функции программы


import telebot
from telebot import types


# объект бота с токеном из @BotFather в телеге
bot = telebot.TeleBot('7322799513:AAFErWKfIx-dKUFzuk7aLNJKsE2YIiRYBqE')



# команда /run, которая запускает логику расчёта стоимости дымохода
@bot.message_handler(commands=['run'])
def run(message):
    a = 0