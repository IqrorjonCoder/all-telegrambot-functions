from telegram.ext import Updater, CommandHandler


def send_poll(update, context):
    update.effective_user.send_poll(question="is this an exmaple poll?",
                                    options=[
                                        "yes !",
                                        "no !",
                                    ],
                                    is_anonymous=False)



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_poll))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()