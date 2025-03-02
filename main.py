import telebot
from telebot import types



# объект бота с токеном из @BotFather в телеге
bot = telebot.TeleBot('7322799513:AAFErWKfIx-dKUFzuk7aLNJKsE2YIiRYBqE')
# временный объект, запоминающий значения
string = []



# обработка команды запуска бота /start
@bot.message_handler(commands=['start'])
def main(message):
    string = []
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🔥 Запустить бота 🔥', callback_data='run'))
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://tstroy33.ru'))
    markup.add(types.InlineKeyboardButton('Перейти на ТГ канал', url='https://t.me/Tstroy33'))

    bot.reply_to(message,
                     f'Привет, {message.from_user.first_name}! \nЭто я - твой бот для расчёта стоимости установки дымохода :)',
                     reply_markup=markup)


# обработка команд /site и /website, которые перекидывают пользователя на оф. сайт ТС
@bot.message_handler(commands=['site', 'website'])
def site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('⚒️ Наш сайт ⚒️', url='https://tstroy33.ru'))
    bot.send_message(message.chat.id, 'Перейти на сайт:', reply_markup=markup)

# обработка команд /tg, /channel и /tgchannel, которые перекидывают пользователя на оф. канал ТС
@bot.message_handler(commands=['tg', 'channel', 'tgchannel'])
def tg_channel(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🗣 Наш ТГ канал 🗣', url='https://t.me/Tstroy33'))
    bot.send_message(message.chat.id, 'Перейти на канал:', reply_markup=markup)

# команда /help, помогающая пользователю разобраться с работой бота
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '🔧 Как работает наш бот?\n\n'
                                      'Для начала введите команду /start.'
                                      'В открывшемся окне нажмите на кнопку <<Запустить бота>>.\n'
                                      'Далее в окнах нажимайте на кнопки с необходимыми для '
                                      'Вас значениями расчёта.\n\n'
                                      'Для завершения работы и получения результатов\b'
                                      ' необходимо в последнем блоке нажать кнопку <<Поставить зонт>>.')



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'run':
        material_selection(callback)
    elif callback.data == 'stainless_stainless_1':
        stainless_stainless_1(callback)
    elif callback.data == 'stainless_stainless_05':
        stainless_stainless_05(callback)
    elif callback.data == 'stainless_galvanized_1':
        stainless_galvanized_1(callback)
    elif callback.data == 'stainless_galvanized_05':
        stainless_galvanized_05(callback)
    elif callback.data == 'd115':
        d115(callback)
    elif callback.data == 'd120':
        d120(callback)
    elif callback.data == 'd130':
        d130(callback)
    elif callback.data == 'd150':
        d150(callback)
    elif callback.data == 'd180':
        d180(callback)
    elif callback.data == 'd200':
        d200(callback)
    elif callback.data == 'd250':
        d250(callback)
    elif callback.data == 'd300':
        d300(callback)
    elif callback.data == 'flue_from_wall':
        flue_from_wall(callback)
    elif callback.data == 'flue_from_ceiling':
        flue_from_ceiling(callback)
    elif callback.data == 'pipe_selection_1m':
        pipe_selection_1m(callback)
    elif callback.data == 'pipe_selection_05m':
        pipe_selection_05m(callback)
    elif callback.data == 'pipe_selection_025m':
        pipe_selection_025m(callback)
    elif callback.data == 'pipe_selection_angle45':
        pipe_selection_angle45(callback)
    elif callback.data == 'pipe_selection_angle90':
        pipe_selection_angle90(callback)
    elif callback.data == 'pipe_selection_monotermo_150and210':
        pipe_selection_monotermo_150and210(callback)
    elif callback.data == 'pipe_selection_monotermo_150and250':
        pipe_selection_monotermo_150and250(callback)
    elif callback.data == 'sandwich_pipe_selection_1m':
        sandwich_pipe_selection_1m(callback)
    elif callback.data == 'sandwich_pipe_selection_05m':
        sandwich_pipe_selection_05m(callback)
    elif callback.data == 'sandwich_pipe_selection_025m':
        sandwich_pipe_selection_025m(callback)
    elif callback.data == 'sandwich_pipe_selection_angle45':
        sandwich_pipe_selection_angle45(callback)
    elif callback.data == 'sandwich_pipe_selection_angle90':
        sandwich_pipe_selection_angle90(callback)
    elif callback.data == 'sandwich_pipe_selection_angle90':
        sandwich_pipe_selection_angle90(callback)
    elif callback.data == 'tee_angle45':
        tee_angle45(callback)
    elif callback.data == 'tee_angle90':
        tee_angle90(callback)
    elif callback.data == 'condensate_collector_yes':
        condensate_collector_yes(callback)
    elif callback.data == 'condensate_collector_no':
        condensate_collector_no(callback)
    elif callback.data == 'mounting_platform_with_brackets':
        mounting_platform_with_brackets(callback)
    elif callback.data == 'mounting_platform_with_long_brackets':
        mounting_platform_with_long_brackets(callback)
    elif callback.data == 'mounting_platform_with_nothing':
        mounting_platform_with_nothing(callback)
    elif callback.data == 'sandwich_pipe_or_umbrella_selection_1m':
        sandwich_pipe_or_umbrella_selection_1m(callback)
    elif callback.data == 'sandwich_pipe_or_umbrella_selection_05m':
        sandwich_pipe_or_umbrella_selection_05m(callback)
    elif callback.data == 'sandwich_pipe_or_umbrella_selection_025m':
        sandwich_pipe_or_umbrella_selection_025m(callback)
    elif callback.data == 'sandwich_pipe_or_umbrella_selection_angle45':
        sandwich_pipe_or_umbrella_selection_angle45(callback)
    elif callback.data == 'sandwich_pipe_or_umbrella_selection_angle90':
        sandwich_pipe_or_umbrella_selection_angle90(callback)
    elif callback.data == 'umbrella':
        umbrella(callback)


# блок <<ВЫБОР МАТЕРИАЛА>>
def material_selection(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Нерж. + Нерж. 1 мм', callback_data='stainless_stainless_1')
    btn2 = types.InlineKeyboardButton('Нерж. + Нерж. 0,5 мм', callback_data='stainless_stainless_05')
    btn3 = types.InlineKeyboardButton('Нерж. + Оцинк. 1 мм', callback_data='stainless_galvanized_1')
    btn4 = types.InlineKeyboardButton('Нерж. + Оцинк. 0,5 мм', callback_data='stainless_galvanized_05')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    bot.send_message(callback.message.chat.id, 'ВЫБОР МАТЕРИАЛА:', reply_markup=markup)

def stainless_stainless_1(callback):
    string.append('Нерж+Нерж 1 мм')
    inner_diameter_selection(callback)

def stainless_stainless_05(callback):
    string.append('Нерж+Нерж 0,5 мм')
    inner_diameter_selection(callback)

def stainless_galvanized_1(callback):
    string.append('Нерж+Оц 1 мм')
    inner_diameter_selection(callback)

def stainless_galvanized_05(callback):
    string.append('Нерж+Оц 0,5 мм')
    inner_diameter_selection(callback)
# конец блока <<ВЫБОР МАТЕРИАЛА>>


# блок <<ВЫБОР ВНУТРЕННЕГО ДИАМЕТРА>>
def inner_diameter_selection(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('115 мм', callback_data='d115')
    btn2 = types.InlineKeyboardButton('120 мм', callback_data='d120')
    btn3 = types.InlineKeyboardButton('130 мм', callback_data='d130')
    btn4 = types.InlineKeyboardButton('150 мм', callback_data='d150')
    btn5 = types.InlineKeyboardButton('180 мм', callback_data='d180')
    btn6 = types.InlineKeyboardButton('200 мм', callback_data='d200')
    btn7 = types.InlineKeyboardButton('250 мм', callback_data='d250')
    btn8 = types.InlineKeyboardButton('300 мм', callback_data='d300')
    markup.row(btn1, btn2, btn3, btn4)
    markup.row(btn5, btn6, btn7, btn8)
    bot.send_message(callback.message.chat.id, 'ВЫБОР ВНУТРЕННЕГО ДИАМЕТРА:', reply_markup=markup)

def d115(callback):
    string.append('Внутренний диаметр: 115 мм')
    where_flue_go(callback)
def d120(callback):
    string.append('Внутренний диаметр: 120 мм')
    where_flue_go(callback)
def d130(callback):
    string.append('Внутренний диаметр: 130 мм')
    where_flue_go(callback)
def d150(callback):
    string.append('Внутренний диаметр: 150 мм')
    where_flue_go(callback)
def d180(callback):
    string.append('Внутренний диаметр: 180 мм')
    where_flue_go(callback)
def d200(callback):
    string.append('Внутренний диаметр: 200 мм')
    where_flue_go(callback)
def d250(callback):
    string.append('Внутренний диаметр: 250 мм')
    where_flue_go(callback)
def d300(callback):
    string.append('Внутренний диаметр: 300 мм')
    where_flue_go(callback)
# конец блока <<ВЫБОР ВНУТРЕННЕГО ДИАМЕТРА>>


# блок <<КАК ПОЙДЁТ ДЫМОХОД?>>
def where_flue_go(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Через стену', callback_data='flue_from_wall')
    btn2 = types.InlineKeyboardButton('Через потолок', callback_data='flue_from_ceiling')
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(callback.message.chat.id, 'КАК ПОЙДЁТ ДЫМОХОД?', reply_markup=markup)

def flue_from_wall(callback):
    string.append('Дымоход пойдёт через стену')
    pipe_selection(callback)
def flue_from_ceiling(callback):
    string.append('Дымоход пойдёт через потолок')
    pipe_selection(callback)
# конец блока <<КАК ПОЙДЁТ ДЫМОХОД?>>


# блок <<ВЫБОР ТРУБЫ>>
def pipe_selection(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('1 м', callback_data='pipe_selection_1m')
    btn2 = types.InlineKeyboardButton('1/2 м', callback_data='pipe_selection_05m')
    btn3 = types.InlineKeyboardButton('1/4 м', callback_data='pipe_selection_025m')
    btn4 = types.InlineKeyboardButton('Угол 45°', callback_data='pipe_selection_angle45')
    btn5 = types.InlineKeyboardButton('Угол 90°', callback_data='pipe_selection_angle90')
    btn6 = types.InlineKeyboardButton('Переход монотермо 150/210', callback_data='pipe_selection_monotermo_150and210')
    btn7 = types.InlineKeyboardButton('Переход монотермо 150/250', callback_data='pipe_selection_monotermo_150and250')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5)
    markup.add(btn6)
    markup.add(btn7)
    bot.send_message(callback.message.chat.id, 'ВЫБОР ТРУБЫ:', reply_markup=markup)

def pipe_selection_1m(callback):
    string.append('Обычная труба 1м')
    pipe_selection(callback)
def pipe_selection_05m(callback):
    string.append('Обычная труба 0,5м')
    pipe_selection(callback)
def pipe_selection_025m(callback):
    string.append('Обычная труба 0,25м')
    pipe_selection(callback)
def pipe_selection_angle45(callback):
    string.append('Угол 45 градусов')
    pipe_selection(callback)
def pipe_selection_angle90(callback):
    string.append('Угол 90 градусов')
    pipe_selection(callback)
def pipe_selection_monotermo_150and210(callback):
    string.append('Переход моно-термо 150/210')
    sandwich_pipe_selection(callback)
def pipe_selection_monotermo_150and250(callback):
    string.append('Переход моно-термо 150/250')
    sandwich_pipe_selection(callback)
# конец блока <<ВЫБОР ТРУБЫ>>


# блок <<ВЫБОР СЭНДВИЧ ТРУБЫ>>
def sandwich_pipe_selection(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('1 м', callback_data='sandwich_pipe_selection_1m')
    btn2 = types.InlineKeyboardButton('1/2 м', callback_data='sandwich_pipe_selection_05m')
    btn3 = types.InlineKeyboardButton('1/4 м', callback_data='sandwich_pipe_selection_025m')
    btn4 = types.InlineKeyboardButton('Угол 45°', callback_data='sandwich_pipe_selection_angle45')
    btn5 = types.InlineKeyboardButton('Угол 90°', callback_data='sandwich_pipe_selection_angle90')
    btn6 = types.InlineKeyboardButton('Тройник 45°', callback_data='tee_angle45')
    btn7 = types.InlineKeyboardButton('Тройник 90°', callback_data='tee_angle90')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5)
    markup.add(btn6)
    markup.add(btn7)
    bot.send_message(callback.message.chat.id, 'ВЫБОР СЭНДВИЧ ТРУБЫ:', reply_markup=markup)

def sandwich_pipe_selection_1m(callback):
    string.append('Сэндвич труба 1м')
    sandwich_pipe_selection(callback)
def sandwich_pipe_selection_05m(callback):
    string.append('Сэндвич труба 0,5м')
    sandwich_pipe_selection(callback)
def sandwich_pipe_selection_025m(callback):
    string.append('Сэндвич труба 0,25м')
    sandwich_pipe_selection(callback)
def sandwich_pipe_selection_angle45(callback):
    string.append('Угол 45 градусов')
    sandwich_pipe_selection(callback)
def sandwich_pipe_selection_angle90(callback):
    string.append('Угол 90 градусов')
    sandwich_pipe_selection(callback)
def tee_angle45(callback):
    string.append('Тройник 45 градусов')
    is_condensate_collector(callback)
def tee_angle90(callback):
    string.append('Тройник 90 градусов')
    is_condensate_collector(callback)
# конец блока <<ВЫБОР СЭНДВИЧ ТРУБЫ>>


# блок <<ВЗЯТЬ КОНДЕНСАТОСБОРНИК?>>
def is_condensate_collector(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Да', callback_data='condensate_collector_yes')
    btn2 = types.InlineKeyboardButton('Нет', callback_data='condensate_collector_no')
    markup.row(btn1, btn2)
    bot.send_message(callback.message.chat.id, 'ВЗЯТЬ КОНДЕНСАТОСБОРНИК?', reply_markup=markup)

def condensate_collector_yes(callback):
    string.append("Конденсатосборник: Да")
    mounting_platform(callback)
def condensate_collector_no(callback):
    string.append("Конденсатосборник: Нет")
    mounting_platform(callback)
# конец блока <<ВЗЯТЬ КОНДЕНСАТОСБОРНИК?>>


# блок <<ЧТО ВЗЯТЬ К МОНТАЖНОЙ ПЛОЩАДКЕ?>>
def mounting_platform(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Опору и обычные\nкронштейны', callback_data='mounting_platform_with_brackets')
    btn2 = types.InlineKeyboardButton('Опору и удлинённые\nкронштейны', callback_data='mounting_platform_with_long_brackets')
    btn3 = types.InlineKeyboardButton('Ничего', callback_data='mounting_platform_with_nothing')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_message(callback.message.chat.id, 'ЧТО ВЗЯТЬ К МОНТАЖНОЙ ПЛОЩАДКЕ?', reply_markup=markup)

def mounting_platform_with_brackets(callback):
    string.append('Монтажная площадка с: опорой и обычными кронштейнами')
    sandwich_pipe_or_umbrella_selection(callback)
def mounting_platform_with_long_brackets(callback):
    string.append('Монтажная площадка с: опорой и удлинёнными кронштейнами')
    sandwich_pipe_or_umbrella_selection(callback)
def mounting_platform_with_nothing(callback):
    string.append('Монтажная площадка с: ничем')
    sandwich_pipe_or_umbrella_selection(callback)
# конец блока <<ЧТО ВЗЯТЬ К МОНТАЖНОЙ ПЛОЩАДКЕ?>>


# блок <<ВЫБОР СЭНДВИЧ ТРУБЫ ИЛИ ЗОНТА>>
def sandwich_pipe_or_umbrella_selection(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('1 м', callback_data='sandwich_pipe_or_umbrella_selection_1m')
    btn2 = types.InlineKeyboardButton('1/2 м', callback_data='sandwich_pipe_or_umbrella_selection_05m')
    btn3 = types.InlineKeyboardButton('1/4 м', callback_data='sandwich_pipe_or_umbrella_selection_025m')
    btn4 = types.InlineKeyboardButton('Угол 45°', callback_data='sandwich_pipe_or_umbrella_selection_angle45')
    btn5 = types.InlineKeyboardButton('Угол 90°', callback_data='sandwich_pipe_or_umbrella_selection_angle90')
    btn6 = types.InlineKeyboardButton('Зонт', callback_data='umbrella')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5)
    markup.add(btn6)
    bot.send_message(callback.message.chat.id, 'ВЫБОР СЭНДВИЧ ТРУБЫ:', reply_markup=markup)

def sandwich_pipe_or_umbrella_selection_1m(callback):
    string.append('Сэндвич труба 1м')
    sandwich_pipe_or_umbrella_selection(callback)
def sandwich_pipe_or_umbrella_selection_05m(callback):
    string.append('Сэндвич труба 0,5м')
    sandwich_pipe_or_umbrella_selection(callback)
def sandwich_pipe_or_umbrella_selection_025m(callback):
    string.append('Сэндвич труба 0,25м')
    sandwich_pipe_or_umbrella_selection(callback)
def sandwich_pipe_or_umbrella_selection_angle45(callback):
    string.append('Угол 45 градусов')
    sandwich_pipe_or_umbrella_selection(callback)
def sandwich_pipe_or_umbrella_selection_angle90(callback):
    string.append('Угол 90 градусов')
    sandwich_pipe_or_umbrella_selection(callback)
# конец блока <<ВЫБОР СЭНДВИЧ ТРУБЫ ИЛИ ЗОНТА>>



# БЛОК ОБЩИХ ФУНКЦИЙ

# функция кнопки <<Зонт>>
def umbrella(callback):
    string.append('Зонт')
    end_of_bot_work(callback)

# функция окончания работы бота и подведения итогов
def end_of_bot_work(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(callback.message.chat.id, 'Конец работы бота!')
    bot.send_message(callback.message.chat.id, 'ИТОГ:\n\n' + "\n".join(string))
    bot.send_message(callback.message.chat.id, 'Перезапустить бота: /start')

# КОНЕЦ БЛОКА ОБЩИХ ФУНКЦИЙ


# грубо говоря, бесконечный цикл, позволяющий не прекращать работу (выключится программа - выключится бот)
bot.polling(none_stop=True)
