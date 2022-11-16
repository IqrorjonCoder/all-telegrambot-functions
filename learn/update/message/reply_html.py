from telegram.ext import Updater, Filters, MessageHandler, CommandHandler


def reply_html(update, context):
    update.message.reply_html("""
        <b>salomlar</b>
        <i>bu italiya</i>
    """, allow_sending_without_reply=True)


def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_html))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()