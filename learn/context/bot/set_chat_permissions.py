from telegram.ext import Updater, CommandHandler
from telegram import ChatPermissions


def set_chat_permissions(update, context):
    x = context.bot.set_chat_permissions(chat_id=update.effective_chat.id,
                                         permissions=ChatPermissions(can_send_messages=False,can_send_media_messages=False))
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_chat_permissions))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()