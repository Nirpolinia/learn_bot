import logging #включаем логирование
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters # компонент, который получает/передает сообщения, реагирует на сообщения

import settings #прячем секретный код ботика 

logging.basicConfig(filename='bot.log', level=logging.INFO) #настраиваем файл, куда будет логироваться и уровень важности 

def greet_user (update, context): #update - то, что прило от Телеграмма; context - отдавать команды боту внутри функции
    print('вызван/start')
    update.message.reply_text ("Hi, beauty") #здоровается
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text) #отправить пользователю его же сообщение 
def main ():
    mybot=Updater(settings.API_KEY, use_context=True) #request_kwargs=PROXY - нужно для обхождения блокировок
    dp = mybot.dispatcher #ввсодим сокращения, чтобы уменьшить колличсетво кода 
    dp.add_handler(CommandHandler("start", greet_user )) #название команды без черточки
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) #будет перехватывать сообщения, но не будет перехватывать команды тк добавлем его послеб 


    logging.info("Бот стартовал") #логгируем старт бота
    mybot.start_polling() #регулярные обращения для обновлений
    mybot.idle() #крутись постоянно пока мы тебя не остановим
main() #вызов функции
