from telegram.ext import Updater, CommandHandler


def get_custom_emoji_stickers(update, context):
    stickers = context.bot.get_custom_emoji_stickers(custom_emoji_ids=['5389102131527556772'])
    for i in stickers:
        update.message.reply_text(f"stickers: {i.to_json()}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_custom_emoji_stickers))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()