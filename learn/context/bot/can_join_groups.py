from telegram.ext import Updater, CommandHandler


def can_join_groups(update, context):
    update.message.reply_text(f"can_join_groups : \n*{context.bot.can_join_groups}*", parse_mode="Markdown")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', can_join_groups))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()