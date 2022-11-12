from telegram.ext import Updater, Filters, MessageHandler


def caption_entities(update, context):
    for i, v in enumerate(update.message.caption_entities):
        update.message.reply_text(f"*{i}* : {v.to_json()}\n\n\n", parse_mode="Markdown")
        print(dir(v))


def runner():
    updater = Updater(token="5693888427:AAFE-_nYnUSOxtgDu-hXprZgUvyrLxS_KTE")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.animation, caption_entities))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishlamoqda ...")
    runner()