from telegram.ext import Updater, MessageHandler, Filters


def new_chat_title(update, context):
    update.message.reply_text(f"your changed channel name ... \n\n {update.message.new_chat_title}")

def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_title, new_chat_title))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()