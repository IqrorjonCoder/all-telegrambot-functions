from telegram.ext import Updater, CommandHandler


def export_chat_invite_link(update, context):
    update.message.reply_text(f"invite links : {context.bot.export_chat_invite_link(update.message.chat_id)}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', export_chat_invite_link))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()