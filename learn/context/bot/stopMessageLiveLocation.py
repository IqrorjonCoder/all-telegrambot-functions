from telegram.ext import Updater, CommandHandler


def stopMessageLiveLocation(update, context):
    x = context.bot.stopMessageLiveLocation(chat_id=update.effective_chat.id,
                                               message_id=update.message.message_id-1)
    update.message.reply_text(f"location : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', stopMessageLiveLocation))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()