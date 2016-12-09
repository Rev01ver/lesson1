from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from xml.etree import ElementTree as ET
import urllib.request
import datetime

#CommandHandler - класс для обработки команд

#приветствие пользователя
def greet_user(bot,update): # update - то, что прислал телеграмм?
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Приветствую тебя человек. Этот бот может:\n'
                                                 '- немного поболтать\n'
                                                 '- показывать курс валют /valuta\n'



                    )  #ид чата и текст

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
    today = datetime.date.today()
    rub_dollar = "$ = " + str(rub_dollar)
    rub_evro = "€ = " + str(rub_evro)
    date = "Курсы валют на: " + str(today.strftime("%A, %d %B, %Y"))
    bot.sendMessage(update.message.chat_id, date)
    bot.sendMessage(update.message.chat_id, rub_dollar)
    bot.sendMessage(update.message.chat_id, rub_evro)


#обработка ошибок
def show_error(bot,update, error):
    print('Update "{}" caused error "{}"'.format(update,error)) #на место {} подставляются значения из format

#отвечаем на сообщения
def talk_to_me(bot,update):
    print('Пришло сообщение: {}'.format(update.message.text))
    bot.sendMessage(update.message.chat_id, get_answer(update.message.text,answers))

answers = {"привет":"Привет!",
           "здарова":"здоровее видали",
           "как дела":"Нормально, не жалуюсь. Ты как?",
           "пока":"Ты это, заходи, если чё",
           "нормально":"Мой дедушка сказал бы тебе, что надо всегда говорить ""Хорошо""",
           "плохо":"У кого-то ещё хуже, держись",
           "хорошо":"Красавчег",
           "какой смысл жизни?":"ты далек от его понимания, если спрашиваешь у меня ;)",
           "купи слона":"купилка не выросла :("

           }

def get_answer(question,answers):
    return answers.get(question,"Извини, не понял тебя((. Я только учусь")

#запуск самого бота
def run_bot ():
    updater = Updater("323448045:AAHKhwI_4oVHuUjX3R4aELOOlk92TGWhyJY")
    dp = updater.dispatcher #диспетчер, который распределяет информацию
    dp.add_handler(CommandHandler("start",greet_user))   # диспетчер добавь обработчик команд, типа commanhadler и что обрабатывать
    dp.add_handler(CommandHandler("valuta",dollar_evro))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error) # обработка ошибок - вызываем функцию, которая отображает ошибки
    updater.start_polling() #жди сообщения от телеграмма
    updater.idle() # работай, пока не остановят - ожидание

# чтобы при импорте не запускался код
if __name__ == '__main__':
    run_bot()