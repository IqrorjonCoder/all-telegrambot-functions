from telegram.ext import Updater, CommandHandler


def getUserProfilePhotos(update, context):
    user_pic = context.bot.getUserProfilePhotos(user_id=update.effective_user.id)
    update.message.reply_text(f"profile pictures : \n\n{user_pic}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', getUserProfilePhotos))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()