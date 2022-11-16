from telegram.ext import Updater, MessageHandler, Filters


def parse_caption_entity(update, context):
    update.message.reply_text(f"hi ... \n\n {update.message.parse_caption_entity()}")
    print(update.message.parse_caption_entities())


def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.photo, parse_caption_entity))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()