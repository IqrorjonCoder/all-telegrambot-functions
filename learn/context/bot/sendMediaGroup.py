from telegram.ext import Updater, CommandHandler
from telegram import InputMediaDocument


def sendMediaGroup(update, context):
    context.bot.sendMediaGroup(chat_id=update.effective_chat.id,
                                 media=[
                                     InputMediaDocument(media=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_telegrambot_functions/learn/context/bot/sendMediaGroup.py', 'rb'), caption="firstt filee"),
                                     InputMediaDocument(media=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_telegrambot_functions/learn/context/bot/sendMediaGroup.py', 'rb'), caption="firstt filee"),
                                 ])


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sendMediaGroup))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()