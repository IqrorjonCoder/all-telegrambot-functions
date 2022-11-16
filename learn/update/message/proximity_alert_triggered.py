from telegram.ext import Updater, Filters, MessageHandler


def proximity_alert_triggered(update, context):

    update.message.reply_text("salom ...")
    print(update.message.proximity_alert_triggered)



def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, proximity_alert_triggered))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()