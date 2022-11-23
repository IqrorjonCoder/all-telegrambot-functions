from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def reply_to_message(update, context):
    update.message.reply_text("hello ...")
    update.message.reply_text(f"you replied this message : \n\n\n*{update.message.reply_to_message['text']}*", parse_mode="Markdown")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, reply_to_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
