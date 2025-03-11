import telebot
from telebot import types

bot = telebot.TeleBot("7101274076:AAFEZw0Vm4dEpNto74i6sTWpUFeppwii2kU")
BUTTONS = ["Новая задача ", "Список дел"]
dela = []
dni = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
time = []
TASK_BUTTONS = ["✅","❌","🗓️","🕒"]
class Task:
    def __init__(self, name, time='', day=''):
        self.name = name
        self.time = time
        self.day = day

hour = 8
i = 13
while i > 0:
    if hour == 20:
        time.append(f"{hour}:00")
    else:
        time.append(f"{hour}:00")
        time.append(f"{hour}:30")
    i -=1
    hour +=1
def redactirovanie():
    markup = types.InlineKeyboardMarkup(row_width=4)

    for i in TASK_BUTTONS:
        btn = types.InlineKeyboardButton(i, callback_data=i)
        markup.add(btn)
    return markup
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ntb = types.KeyboardButton(BUTTONS[0])
    lb = types.KeyboardButton(BUTTONS[1])
    markup.row(ntb, lb)
    bot.send_message(message.chat.id, "Привет")
    bot.send_message(message.chat.id, "Напиши 'Новая задача' для добавления новой задачи или 'Список дел' для просмотра твоего списка")
    bot.send_message(message.chat.id, "Что надо сделать?", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == BUTTONS[0]:
        bot.send_message(message.chat.id, "Введите название задачи")
    elif message.text == BUTTONS[1]:
        text = ""
        if len(dela) == 0:
            text = "У вас нет дел. Завидую"
        else:
             for i, j in enumerate(dela):
                text += f"Задача №{i+1}: {j.name}\n"
        bot.send_message(message.chat.id, text, reply_markup=redactirovanie())
    else:
        new_task = Task(message.text)
        dela.append(new_task)
        bot.send_message(message.chat.id, f"Добавлена задача {new_task.name}")

        keyboard = types.InlineKeyboardMarkup(row_width=4)
        keyboardbtn = []
        for i in dni:
            btn = types.InlineKeyboardButton(i, callback_data=i)
            keyboardbtn.append(btn)
        keyboard.add(*keyboardbtn)
        bot.send_message(message.chat.id, "Выберите день для выполнения задачи", reply_markup=keyboard)

        keyboard1 = types.InlineKeyboardMarkup(row_width=5)
        keyboardbtn1 = []
        for i in time:
            btn1 = types.InlineKeyboardButton(i, callback_data=i)
            keyboardbtn1.append(btn1)
        keyboard1.add(*keyboardbtn1)
        bot.send_message(message.chat.id, "Выберите время для выполнения задачи", reply_markup=keyboard1)
@bot.callback_query_handler(func=lambda call:True)
def dayselect(call):
    print(call.data)
    if len(dela)>0:
        dela[-1].day = call.data
    bot.edit_message_text(f"Запланировано на {call.data}", call.message.chat.id, call.message.message_id)
    bot.answer_callback_query(call.id)
@bot.callback_query_handler(func=lambda call:True)
def timeselect(call):
    if len(dela)>0:
        dela[-1].time = call.data
    bot.edit_message_text(f"Запланировано на {call.time}", call.message.chat.id, call.message.message_id)
    bot.answer_callback_query(call.id)

bot.polling(non_stop=True, interval=0)
