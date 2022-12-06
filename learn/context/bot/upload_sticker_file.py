from telegram.ext import Updater, CommandHandler


def upload_sticker_file(update, context):
    x = context.bot.upload_sticker_file(user_id=update.effective_user.id,
                                        png_sticker=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_telegrambot_functions/base/google_png.jpg', 'rb'))
    update.message.reply_text(f"upload_sticker_file : {x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', upload_sticker_file))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
