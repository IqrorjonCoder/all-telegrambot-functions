from telegram.ext import Updater, CommandHandler


def sendVoice(update, context):
    context.bot.sendVoice(chat_id=update.effective_chat.id,
                           voice=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_telegrambot_functions/base/example_voice.ogg', 'rb'),
                           caption="simplee caption")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sendVoice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()