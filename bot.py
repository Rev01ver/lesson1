from telegram.ext import Updater,CommandHandler,MessageHandler,Filters


#приветствие пользователя
def greet_user(bot,update): # update - то, что прислал телеграмм?
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Готов к унижениям слабак?')  #ид чата и текст


#обработка ошибок
def show_error(bot,update, error):
    print('Update "{}" caused error "{}"'.format(update,error)) #на место {} подставляются значения из format


#отвечаем на сообщения
def talk_to_me(bot,update):
    print('Пришло сообщение: {}'.format(update.message.text))
    bot.sendMessage(update.message.chat_id, update.message.text)

def main ():
    updater = Updater("323448045:AAHKhwI_4oVHuUjX3R4aELOOlk92TGWhyJY")
    dp = updater.dispatcher #диспетчер, которые распределяет информацию
    dp.add_handler(CommandHandler("start",greet_user))   # испетчер добавь обработчик команд, типа commanhadler и что обрабатывать
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error) # обработка ошибок - вызываем функцию, которая отображает ошибки
    updater.start_polling() #жди сообщения от телеграмма\

    updater.idle() # работай, пока не остановят

if __name__ == '__main__': # чтобы при импорте не запускался код
    main()



