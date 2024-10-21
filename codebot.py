# Импортируем библиотеки пайтон
import telebot
import datetime
import time
from telebot import types

# Токен бота, который выдается в процессе создания бота Telegram, вставляем вместо 'ваш токен'
bot = telebot.TeleBot('7830171145:AAEOU0N9FDRUbehoUpo_4GZYFsTPuFRKtlc')
# Обработка команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет, я бот с расписанием занятий! Выберите действие:", reply_markup=keyboard)

# Создание клавиатуры с кнопками
keyboard = types.ReplyKeyboardMarkup(row_width=1)
button1 = types.KeyboardButton("Расписание")
button2 = types.KeyboardButton("Дедлайны")
button3 = types.KeyboardButton("Каникулы и сессии")
keyboard.add(button1, button2, button3)



# Обработка нажатий на кнопки
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Расписание":
        bot.send_message(1984839991, format_schedule(get_today_schedule()))
    elif message.text == "Дедлайны":
        bot.reply_to(message, "тут пока ничего нет(")
    elif message.text == "Каникулы и сессии":
        bot.reply_to(message, "тут пока ничего нет(")

# Список с расписанием занятий, Чётная = Schedule 2, Нечётная  Schedule 1
schedule1 = {
    'Monday': [
    
     ],
    'Tuesday': [
        {'Время': '9:30 - 10:50', 'Предмет': 'БП-126, лекция, Дискретная математика (Мокеев Д.Б.'},
        {'Время': '11:10 - 12:30', 'Предмет': 'БП-405, семинар, Электроснабжение железных дорог (Цаплина Е.К.)'},
        {'Время': '13:00 - 14:20', 'Предмет': 'БП-406, семинар, Математический анализ (Чистякова С.А.)'},
    ],
    'Wednesday': [
        {'Время': '9:30 - 10:50', 'Предмет': 'Л-318, семинар, Линейная алгебра и геометрия (Беспалов П.А.)'},
        {'Время': '11:10 - 12:30', 'Предмет': 'Л-323, лекция, Программирование С/С++ (Пеплин Ф.С.)'},
        {'Время': '13:00 - 14:20', 'Предмет': 'Л-225, лекция, Линейная алгебра и геометрия (Савина О.Н.)'},
        {'Время': '14:40 - 16:00', 'Предмет': 'БП-406, семинар, Математический анализ (Чистяков В.В.)'},
    # ],
    # 'Thursday': [

    ],
    'Friday': [
        {'Время': '13:00 - 14:20', 'Предмет': 'online, семинар, Основы Российской Государственности (Константинова Т.Н.)'},
        {'Время': '14:40 - 16:00', 'Предмет': 'online, семинар, История России (Константинова Т.Н.)'},
    ],
    'Saturday':[
        {'Время': '8:00 - 9:20', 'Предмет': 'Л-325, Английский язык (Черницкая М.Б.)'},
        {'Время': '9:30 - 10:50', 'Предмет': 'Л-325, Английский язык (Черницкая М.Б.)'}
    ]
}

 # Дни недели можно удалять или добавлять. Главное сохранить синтаксис списка, не потерять символы. Название дня недели должно быть на английском языке.
schedule2 = {
    'Monday': [
        {'Время': '11:10 - 12:30', 'Предмет': 'БП-216, практика, Программирование на С++'},
        {'Время': '13:00 - 14:20', 'Предмет': 'БП-216, практика, Программирование на С++'},
    ],
    'Tuesday': [
        {'Время': '9:30 - 10:50', 'Предмет': 'БП-126, лекция, Дискретная математика (Мокеев Д.Б.'},
        {'Время': '11:10 - 12:30', 'Предмет': 'БП-405, семинар, Электроснабжение железных дорог (Цаплина Е.К.)'},
        {'Время': '13:00 - 14:20', 'Предмет': 'БП-406, семинар, Математический анализ (Чистякова С.А.)'},
    ],
    'Wednesday': [
        {'Время': '9:30 - 10:50', 'Предмет': 'Л-318, семинар, Линейная алгебра и геометрия (Беспалов П.А.)'},
        {'Время': '11:10 - 12:30', 'Предмет': 'Л-323, лекция, Программирование С/С++ (Пеплин Ф.С.)'},
        {'Время': '13:00 - 14:20', 'Предмет': 'Л-225, лекция, Линейная алгебра и геометрия (Савина О.Н.)'},
        {'Время': '14:40 - 16:00', 'Предмет': 'БП-406, семинар, Математический анализ (Чистяков В.В.)'},
    # ],
    # 'Thursday': [

    ],
    'Friday': [
        {'Время': '13:00 - 14:20', 'Предмет': 'online, семинар, Основы Российской Государственности (Константинова Т.Н.)'},
        {'Время': '14:40 - 16:00', 'Предмет': 'online, семинар, История России (Константинова Т.Н.)'},
    ],
    'Saturday':[
    ]
}

now = datetime.datetime.now()        # Получаем текущую дату с помощью библиотеки datetime
week_number = now.isocalendar()[1]   # Получаем номер недели в году с помощью библиотеки datetime

# Функция для получения расписания на текущий день
def get_today_schedule():
    current_day = datetime.datetime.now().strftime("%A")  # current_day получает ответ в виде дня недели на английском языке с помощью библиотеки datetime
    if week_number % 2 == 0 and current_day in schedule2: # Если условие (деление номера недели на 2 без остатка) верно и в списке есть день, который совпадает с текущим,
        return schedule2[current_day]                     # функция вернёт ответ в виде списка Schedule 2
    elif current_day in schedule1:                        # Если условие деления не верно, функция вернёт ответ в виде списка Schedule 1
        return schedule1[current_day]
    else:                                                 # Если в списке нет текущего дня недели, функция вернёт пустой ответ
        return []

# Функция для форматированного вывода расписания в текстовом формате
def format_schedule(schedule):
    if not schedule:                                                     # Если функция get_today_schedule вернула пустой ответ,
        return "Сегодня пар нет!"                                        # функиця format_schedule вернёт ответ "Сегодня пар нет!"
    else:                                                                # Если функция get_today_schedule вернула ответ в виде одного из списков, format_schedule вернёт ответ в виде переменной result
        result = "Расписание на сегодня:\n"                              # переменная result имеет вид string (по русски = строка), Символ новой строки в Python — это \n . Он используется для обозначения окончания строки текста
        for lesson in schedule:                                          # for in - это цикл. Общий синтаксис for... in в python выглядит следующим образом: for <переменная> in <последовательность>:< действие> else:< действие>.
            result += f"{lesson['Время']} - {lesson['Предмет']}\n"       # Элементы «последовательности» перебираются один за другим «переменной» цикла; если быть точным, переменная указывает на элементы.
        return result                                                    # "+-" - это инкрементальные конкатенации в цикле. Тема не самая простая, об этом позже. f-строки позволяют форматировать информацию в нужном нам виде


# Функция для отправки расписания на текущий день в чат
def send_today_schedule(chat_id):
    bot.send_message(chat_id, format_schedule(get_today_schedule()))     # bot.send_message отправляет данные в чат с ботом

# Задаем обработчик команды /schedule
# @bot.message_handler(commands=['schedule'])
# def send_schedule(message):
#     send_today_schedule('1984839991')        # Вместо "айди чата с ботом" вставляем chatid своего чата

# Определяем интервал для автоматической отправки расписания
# interval = 60 * 60  # Отправлять расписание каждый час (измеряется в секундах, поэтому 60 сек * 60 = 1 час)
# Запускаем цикл для автоматической отправки расписания
# while True:
#     send_today_schedule('1984839991')  # Замените <chat_id> на идентификатор нужного чата
#     time.sleep(interval)                      # time.sleep запускает таймер ожидания с перменной interval

bot.polling(none_stop=True, interval=0)   # Запускаем бота
#В этом примере бот отвечает на команду /schedule отправкой расписания занятий на текущий день в чат.
# Также цикл While отправляет расписание в заданный чат каждый заданный интервал времени.
# Вы можете использовать этот пример как основу для своего Telegram-бота с расписанием занятий и автоматической отправкой.
