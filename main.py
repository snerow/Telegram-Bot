import telebot
from telebot import types


# объект бота с токеном из @BotFather в телеге
bot = telebot.TeleBot('7322799513:AAFErWKfIx-dKUFzuk7aLNJKsE2YIiRYBqE')


# обработка команды запуска бота /start
@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Запустить бота', callback_data='run'))
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://tstroy33.ru'))
    bot.reply_to(message,
                     'Привет, Егор! \nЭто я - твой будущий бот для расчёта стоимости установки дымоходов :)',
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'run':
        bot.reply_to(callback.message, 'Я работаю!')
        material_selection(callback.message)

def material_selection(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Нерж. + Нерж. 1 мм', url='https://tstroy33.ru')
    btn2 = types.InlineKeyboardButton('Нерж. + Нерж. 0,5 мм', url='https://tstroy33.ru')
    btn3 = types.InlineKeyboardButton('Нерж. + Оцинк. 1 мм', url='https://tstroy33.ru')
    btn4 = types.InlineKeyboardButton('Нерж. + Оцинк. 0,5 мм', url='https://tstroy33.ru')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)

    bot.send_message(message.chat.id, 'Выбор материала:', reply_markup=markup)



# грубо говоря, бесконечный цикл, позволяющий не прекращать работу (выключится программа - выключится бот)
bot.polling(none_stop=True)
