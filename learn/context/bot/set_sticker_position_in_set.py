from telegram.ext import Updater, CommandHandler


def set_sticker_position_in_set(update, context):
    x = context.bot.set_sticker_position_in_set(sticker='sticker',
                                                position=10)
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_sticker_position_in_set))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()