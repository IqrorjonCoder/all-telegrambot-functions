from telegram.ext import Updater, CommandHandler


def uploadStickerFile(update, context):
    x = context.bot.uploadStickerFile(user_id=update.effective_user.id,
                                        png_sticker=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_telegrambot_functions/base/google_png.jpg', 'rb'))
    update.message.reply_text(f"uploadStickerFile : {x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', uploadStickerFile))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
