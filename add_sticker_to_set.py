from telegram.ext import Updater, CommandHandler


def add_sticker_to_set(update, context):
    update.message.reply_text("salomcha ...")
    context.bot.add_sticker_to_set(user_id=update.effective_user.id,
                                   name="simple sticker",
                                   emojis="simple emojis")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', add_sticker_to_set))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()