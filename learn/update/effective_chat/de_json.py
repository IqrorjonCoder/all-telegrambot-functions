from telegram.ext import Updater, CommandHandler


def de_json(update, context):
    update.message.reply_text(f"de_json : \n{update.effective_chat.de_json()}")



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', de_json))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()