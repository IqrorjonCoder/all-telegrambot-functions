from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def text_markdown_v2(update, context):
    print(update.message.text_markdown_v2)
    update.message.reply_text(f"text_markdown_v2 is :  {update.message.text_markdown_v2}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', text))
    dispatcher.add_handler(MessageHandler(Filters.text, text_markdown_v2))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

