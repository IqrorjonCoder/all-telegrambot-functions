from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def reply_poll(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_poll(question="what is your firstname?",
                              options=[
                                  "Iqrorjon",
                                  "azamat",
                                  "sherzod",
                                  "humoyun"
                              ])


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_poll))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()