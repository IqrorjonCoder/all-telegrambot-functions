from telegram.ext import Updater, Filters, MessageHandler


def poll(update, context):
    # update.message.reply_poll(question="Bugun darsda kimlar yo'q?",
    #                           options=[
    #                               "Iqrorjon",
    #                               "Sherzodjon",
    #                               "Azamat",
    #                               "Humoyun"
    #                           ],
    #                           is_anonymous=False,
    #                           allows_multiple_answers=True,
    #                           protect_content=False)

    update.message.reply_text("salom ...")
    print(update.message.poll)



def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.poll, poll))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()