from telegram.ext import Updater, CommandHandler


def sendContact(update, context):
    context.bot.sendContact(chat_id=update.effective_chat.id,
                             phone_number="+998903605293",
                             first_name="first namee",
                             last_name="last nanmee")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sendContact))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()