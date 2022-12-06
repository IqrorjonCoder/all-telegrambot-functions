from telegram.ext import Updater, CommandHandler
from telegram import InputMediaDocument


def send_media_group(update, context):
    context.bot.send_media_group(chat_id=update.effective_chat.id,
                                 media=[
                                     InputMediaDocument(media=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_telegrambot_functions/learn/context/bot/send_media_group.py', 'rb'), caption="firstt filee"),
                                     InputMediaDocument(media=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_telegrambot_functions/learn/context/bot/send_media_group.py', 'rb'), caption="firstt filee"),
                                 ])


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_media_group))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()