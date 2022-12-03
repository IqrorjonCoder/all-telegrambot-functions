from telegram.ext import Updater, CommandHandler


def create_new_sticker_set(update, context):
    sticker = context.bot.create_new_sticker_set(user_id=update.effective_user.id,
                                                 name="simpleesticker",
                                                 title="simpleetitle",
                                                 emojis="simpleeemojis",
                                                 png_sticker=open('/Users/student/PycharmProjects/minime/base/AQADccIxGxCQoUsB.jpg', 'rb'))



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', create_new_sticker_set))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()