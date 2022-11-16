from telegram.ext import Updater, MessageHandler, Filters


def parse_caption_entites(update, context):
    update.message.reply_text(f"hii ... \n\n {update.message.parse_caption_entities()}")
    print(update.message.parse_caption_entities())


def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.photo, parse_caption_entites))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()