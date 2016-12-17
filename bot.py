# encoding: utf-8

from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from xml.etree import ElementTree as ET
import urllib.request
from datetime import datetime
import ephem
import locale
import difflib


#CommandHandler - класс для обработки команд

#приветствие пользователя
def greet_user(bot,update): # update - то, что прислал телеграмм?
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Приветствую тебя человек. Этот бот может:\n'
                                                 '- немного поболтать\n'
                                                 '- показывать курс валют /valuta\n'
                                                 '- подсчитываем количество слов в предложении /wordcount\n'
                                                 '- калькулятор /calc\n'
                                                 '- словарный калькулятор /wcalc\n'
                                                 '- рассказать, когда ближайшее полнолуние \n'
                                                 '- играть в слова /goroda \n'





                    )  #ид чата и текст

#goroda
def goroda(bot,update):
    print('Вызван /goroda')
    print('Пришло сообщение: {}'.format(update.message.text))
    n_str = update.message.text
    n_str = n_str.replace("/goroda ", "").replace(" ", "")
    city_next = ""
    if n_str in city_list:
        city_list.remove(n_str)
        for city in city_list:
            if n_str.lower()[-1] == city.lower()[0]:
               city_next = city
               city_list.remove(city)
               bot.sendMessage(update.message.chat_id, text="{}, ваш ход".format(city_next))
               break
        if city_next == "":
            bot.sendMessage(update.message.chat_id, text="Не знаю, что придумать, я проиграл :(")
    else:
        bot.sendMessage(update.message.chat_id, text="Или такого города не существует или он уже был :)"
                        )
city_list = ["Москва","Альметьевск","Абакан","Нижний новгород","Киров","Воркута","Домодедово"]

#word calculator
def wcalc(bot,update):
    print('Вызван /wcalc')
    print('Пришло сообщение: {}'.format(update.message.text))
    n_str = update.message.text
    n_str = n_str.replace("/wcalc сколько будет ","").replace(" ","")
    dot = "."
    if "плюс" in n_str:
        s_str = n_str.split("плюс")
        print(s_str)
        #for i in s_str:
         #   result += int(numbers.get(i))

        result = 0
        for i in s_str:
            result += int(numbers.get(i))

    elif "минус" in n_str:
        s_str = n_str.split("минус")
        result = int(numbers.get(s_str[0]))
        for i in s_str[1:]:
            result -= int(numbers.get(i))

    elif "умножитьна" in n_str:
        s_str = n_str.split("умножитьна")
        result = int(numbers.get(s_str[0]))
        for i in s_str[1:]:
            result *= int(numbers.get(i))

    elif "разделитьна" in n_str:
        s_str = n_str.split("разделитьна")
        result = int(numbers.get(s_str[0]))
        for i in s_str[1:]:
            result /= int(numbers.get(i))

    bot.sendMessage(update.message.chat_id, text="Результат = {}".format(result))


numbers = {"один":1,
           "два":2,
           "три":3,
           "четыре":4,
           "пять":5,
           "шесть":6,
           "семь":7,
           "восемь":8,
           "девять":9

           }





#calculator
def calc(bot,update):
    print('Вызван /calc')
    print('Пришло сообщение: {}'.format(update.message.text))
    # custom_keyboard = [['top-left', 'top-right'],
    #                    ['bottom-left', 'bottom-right']]
    # reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    # # bot.sendMessage(chat_id=chat_id, text="Custom Keyboard Test", reply_markup=reply_markup)
    n_str = update.message.text
    n_str = n_str.replace("/calc ","").replace(" ","")

    if n_str[-1] == "=":
        n_str = n_str[:-1]
        if "+" in n_str:
            s_str = n_str.split("+")

            result = 0
            for i in s_str:
                result += int(i)

        elif "-" in n_str:
            s_str = n_str.split("-")
            result = int(s_str[0])
            for i in s_str[1:]:
                result -= int(i)


        elif "/" in n_str:
            s_str = n_str.split("/")
            if int(s_str[0]) == 0 or int(s_str[1]) == 0:
                bot.sendMessage(update.message.chat_id, text="Извини, деление на 0 запрещено")
            else:
                result = int(s_str[0])
                for i in s_str[1:]:
                    result /= int(i)

        elif "*" in n_str:
            s_str = n_str.split("*")
            result = int(s_str[0])
            for i in s_str[1:]:
                result *= int(i)
        bot.sendMessage(update.message.chat_id, text="Результат = {}".format(result))
    else:
        bot.sendMessage(update.message.chat_id, text="Ты ты не ввел знак = в конеце для подсчета")



#подсчет количества слов в предложении
def wordcount(bot,update):
    print('Вызван /wordcount')
    print('Пришло сообщение: {}'.format(update.message.text))
    if " " in update.message.text:
        count = len(update.message.text.split(" "))
        bot.sendMessage(update.message.chat_id, text="Количество слов в предложении = {}".format(count -1))
    else:
        bot.sendMessage(update.message.chat_id, text="Количество слов в предложении = 1")


#смотрим курсы валют с cbr
def dollar_evro(bot,update):
    """Получает значения доллара и евро в рублях на время запуска. Данные берутся с сайта ЦБР. Возвращает значение доллара в рублях, евро в рублях, дату."""
    print('Вызван /valuta')
    id_dollar = "R01235"
    id_evro = "R01239"
    valuta = ET.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req"))
    for line in valuta.findall('Valute'):
        id_v = line.get('ID')
        if id_v == id_dollar:
            rub_dollar = line.find('Value').text
        if id_v == id_evro:
            rub_evro = line.find('Value').text


    today = datetime.now()
    bot.sendMessage(update.message.chat_id, text="Курс на {}\n$ = {}\n€ = {}".format(today.strftime('%d %B %Y'),rub_dollar,rub_evro))

#обработка ошибок
def show_error(bot,update, error):
    print('Update "{}" caused error "{}"'.format(update,error)) #на место {} подставляются значения из format


#moon predict
def moon_predict(moon_str):
   return (ephem.next_full_moon(str(moon_str[-1])))



#отвечаем на сообщения
def talk_to_me(bot,update):
    print('Пришло сообщение: {}'.format(update.message.text))
    update.message.text = update.message.text.lower()
    #преобразуем в список без пробелов
    moon_str = update.message.text.split(" ")
    #сравниваем два списка
    # d = difflib.Differ()
    moon_str[-1] = moon_str[-1].replace("?", "")
    if moon_str[:-1] == moon_check_list:
        # print(d.compare(moon_str[:-1],moon_check_list))
        bot.sendMessage(update.message.chat_id, str(moon_predict(moon_str)))
    elif moon_str == moon_check_list:
        bot.sendMessage(update.message.chat_id, "Дату не ввел, красавчик")
    else:
        bot.sendMessage(update.message.chat_id, get_answer(update.message.text,answers))



answers = {"привет":"Привет!",
           "здарова":"здоровее видали",
           "как дела":"Нормально, не жалуюсь. Ты как?",
           "пока":"Ты это, заходи, если чё",
           "нормально":"Мой дедушка сказал бы тебе, что надо всегда говорить ""Хорошо""",
           "плохо":"У кого-то ещё хуже, держись",
           "хорошо":"Красавчег",
           "какой смысл жизни?":"Ты далек от его понимания, если спрашиваешь у меня ;)",
           "купи слона":"Купилка не выросла :("

           }
moon_check_list = ['когда', 'ближайшее', 'полнолуние', 'после']


def get_answer(question,answers):
    return answers.get(question,"Извини, не понял тебя((. Я только учусь")

#запуск самого бота
def run_bot ():

    #locale.setlocale(locale.LC_TIME, 'os_RU.UTF-8')
    updater = Updater("323448045:AAHKhwI_4oVHuUjX3R4aELOOlk92TGWhyJY")
    dp = updater.dispatcher #диспетчер, который распределяет информацию
    dp.add_handler(CommandHandler("start",greet_user))   # диспетчер добавь обработчик команд, типа commanhadler и что обрабатывать
    dp.add_handler(CommandHandler("valuta",dollar_evro))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("calc", calc))
    dp.add_handler(CommandHandler("wcalc", wcalc))
    dp.add_handler(CommandHandler("goroda", goroda))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))


    dp.add_error_handler(show_error) # обработка ошибок - вызываем функцию, которая отображает ошибки
    updater.start_polling() #жди сообщения от телеграмма
    updater.idle() # работай, пока не остановят - ожидание

# чтобы при импорте не запускался код
if __name__ == '__main__':
    run_bot()