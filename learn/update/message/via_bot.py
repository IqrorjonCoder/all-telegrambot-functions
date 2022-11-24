from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def via_bot(update, context):
    # 1035463819
    # 1035463819
    # 5333086108

    update.message.reply_text(f"via_bot is : {update.message.via_bot}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.via_bot(bot_id=[5333086108, 1035463819], username=['IqrorjonCoder', '@IqrorjonCoder', '@IqrorjonCoderBot', 'IqrorjonCoderBot']), via_bot))
    # dispatcher.add_handler(MessageHandler(Filters.text, via_bot))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

