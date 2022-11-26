from telegram.ext import Updater, CommandHandler


def send_game(update, context):
    update.message.reply_text("salom ...")
    update.effective_user.send_game(game_short_name="simple game")



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_game))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()