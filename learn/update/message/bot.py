from telegram.ext import Updater, CommandHandler


def bot(update, context):

    update.message.reply_text("salomm")
    # update.message.bot is like the context.bot

    update.message.reply_text(f"@{update.message.bot.username}")


def runner():
    updater = Updater(token='5693888427:AAFE-_nYnUSOxtgDu-hXprZgUvyrLxS_KTE')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', bot))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishlamoqda ...")
    runner()
