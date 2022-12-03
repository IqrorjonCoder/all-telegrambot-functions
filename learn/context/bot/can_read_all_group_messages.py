from telegram.ext import Updater, CommandHandler


def can_read_all_group_messages(update, context):
    update.message.reply_text(f"can_read_all_group_messages : \n*{context.bot.can_read_all_group_messages}*", parse_mode="Markdown")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', can_read_all_group_messages))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()