from telegram.ext import Updater, CommandHandler


def send_animation(update, context):
    context.bot.send_animation(chat_id=update.effective_chat.id,
                               animation=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_telegrambot_functions/base/gif_example.mp4', 'rb'),
                               caption="simplee animation")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_animation))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()