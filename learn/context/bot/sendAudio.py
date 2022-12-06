from telegram.ext import Updater, CommandHandler


def sendAudio(update, context):
    context.bot.sendAudio(chat_id=update.effective_chat.id,
                           audio=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_telegrambot_functions/base/mp3_example.mp3', 'rb'),
                           caption="simplee animation")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sendAudio))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()