from telegram.ext import Updater, CommandHandler


def sender_chat(update, context):
    print(update.message.sender_chat)
    context.bot.send_message(chat_id=update.message.sender_chat, text="saloomchalar!")

    # {'username': 'sinov_iqrorjonbot', 'title': 'sinov', 'type': 'channel', 'id': -1001454217023}


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sender_chat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()