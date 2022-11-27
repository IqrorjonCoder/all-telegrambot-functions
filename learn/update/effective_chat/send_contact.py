from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def send_contact(update, context):
    x = update.effective_chat.send_contact(phone_number="+998 90 627 03 91",
                                       first_name="iqrorjon",
                                       last_name="islomov")
    update.message.reply_text(f"send_contact : \n{x}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_contact))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
