from telegram.ext import Updater, CommandHandler


def set_chat_sticker_set(update, context):
    x = context.bot.set_chat_sticker_set(chat_id=update.effective_chat.id,
                                         sticker_set_name="stickersetname")
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_chat_sticker_set))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()