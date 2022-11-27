from telegram.ext import Updater, CommandHandler


def can_set_sticker_set(update, context):
    update.message.reply_text(f"can_set_sticker_set : {update.effective_chat.can_set_sticker_set}")



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', can_set_sticker_set))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()