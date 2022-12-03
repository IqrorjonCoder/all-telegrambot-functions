from telegram.ext import Updater, CommandHandler


def approve_chat_join_request(update, context):
    print(update.effective_chat.id)
    update.message.reply_text("salom ...")
    context.bot.approve_chat_join_request(chat_id="-1001609283019",
                                          user_id=update.effective_user.id)



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', approve_chat_join_request))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()