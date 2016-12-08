from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import urllib.request
from xml.etree import ElementTree as ET
import datetime

#CommandHandler - класс для обработки команд

#приветствие пользователя
def greet_user(bot,update): # update - то, что прислал телеграмм?
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Приветствую тебя человек. Этот бот может:\n'
                                                 '- показывать курс валют /valuta')  #ид чата и текст


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
    if (update.message.text == "чмо"):
        bot.sendMessage(update.message.chat_id, "Сам такой")
    elif():
        bot.sendMessage(update.message.chat_id, update.message.text)


def dollar_show(bot,update):
    print('Вызван /dollar')
    bot.sendMessage(update.message.chat_id, text='Откуда у тебя деньги?')



def run_bot ():
    updater = Updater("323448045:AAHKhwI_4oVHuUjX3R4aELOOlk92TGWhyJY")
    dp = updater.dispatcher #диспетчер, который распределяет информацию
    dp.add_handler(CommandHandler("start",greet_user))   # диспетчер добавь обработчик команд, типа commanhadler и что обрабатывать
    dp.add_handler(CommandHandler("valuta",dollar_evro))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error) # обработка ошибок - вызываем функцию, которая отображает ошибки
    updater.start_polling() #жди сообщения от телеграмма

    updater.idle() # работай, пока не остановят - ожидание

if __name__ == '__main__': # чтобы при импорте не запускался код
    run_bot()



