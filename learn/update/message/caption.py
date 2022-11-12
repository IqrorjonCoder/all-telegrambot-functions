from telegram.ext import CommandHandler, Updater, Filters, MessageHandler


def caption(update, context):
    print(update.message.caption)
    update.message.reply_text(f"your animation caption text is *{update.message.caption}*", parse_mode="Markdown")


def runner():
    updater = Updater(token="5693888427:AAFE-_nYnUSOxtgDu-hXprZgUvyrLxS_KTE")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.animation, caption))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishlamoqda ...")
    runner()