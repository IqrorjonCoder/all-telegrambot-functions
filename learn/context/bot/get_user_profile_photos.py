from telegram.ext import Updater, CommandHandler


def get_user_profile_photos(update, context):
    user_pic = context.bot.get_user_profile_photos(user_id=update.effective_user.id)
    update.message.reply_text(f"profile pictures : \n\n{user_pic}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_user_profile_photos))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()