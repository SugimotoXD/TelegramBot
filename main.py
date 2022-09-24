import telebot
from telebot import types  # для указание типов
import config

bot = telebot.TeleBot('5790202829:AAE0NUg5uccIaePIdo7efnNIl1Am2BhXd4o')



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("🤫 Основное")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,text="Привет, {0.first_name}! Я бот Калининградского Бизнес Колледжа".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет, привет. Чтобы узнать что я умею нажми на кнопку 'Основное'!)")
    elif (message.text == "🤫 Основное"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        btn3 = types.KeyboardButton("Вывести расписание")
        btn4 = types.KeyboardButton("Вывести новости")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3,btn4, back)
        bot.send_message(message.chat.id, text="Выберите команду", reply_markup=markup)

    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться со студентами, вывести расписание, и многое другое но позже")

    elif message.text == "Вывести новости":
        bot.send_message(message.chat.id, text="Вывожу новости...")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)



    elif message.text == "Вывести расписание":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = types.KeyboardButton("20-ИСП-4")
        button2 = types.KeyboardButton("17-СД-3")
        button3 = types.KeyboardButton("18-ПС-4")
        button4 = types.KeyboardButton("12-КС-1")
        button5 = types.KeyboardButton("12-ПК-5")
        button6 = types.KeyboardButton("21-КРП-3")
        button7 = types.KeyboardButton("21-ПД-1")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1,button2,button3,button4,button5,button6,button7, back)
        bot.send_message(message.chat.id, text="Из какой вы группы ?", reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("🤫 Основное")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


    else:
        bot.send_message(message.chat.id, text="Не урчи, я делаю это, пока без успешно, но делаю")

bot.polling(none_stop=False)
bot.delete_webhook(True)
