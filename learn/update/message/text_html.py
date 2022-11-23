from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def text_html(update, context):
    print(update.message.text_html)
    update.message.reply_text(f"text_html is :  {update.message.text_html}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', text))
    dispatcher.add_handler(MessageHandler(Filters.text, text_html))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

