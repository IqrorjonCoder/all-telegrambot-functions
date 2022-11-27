from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def send_poll(update, context):
    update.effective_chat.send_poll(question="qhat is your name?",
                                    options=[
                                        "iqrorjon",
                                        "azamat",
                                        "humoyun"
                                    ])


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_poll))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
