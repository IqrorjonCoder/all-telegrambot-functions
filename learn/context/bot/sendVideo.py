from telegram.ext import Updater, CommandHandler


def sendVideo(update, context):
    context.bot.sendVideo(chat_id=update.effective_chat.id,
                           video=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_telegrambot_functions/base/example_video.mp4', 'rb'),
                           caption="simplee video")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sendVideo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()