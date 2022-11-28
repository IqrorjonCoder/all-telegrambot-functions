from telegram.ext import Updater, CommandHandler


def addStickerToSet(update, context):
    update.message.reply_text("salomcha ...")
    context.bot.addStickerToSet(user_id=update.effective_user.id,
                                   name="simple sticker",
                                   emojis="simple emojis")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', addStickerToSet))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()