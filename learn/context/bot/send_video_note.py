from telegram.ext import Updater, CommandHandler


def send_video_note(update, context):
    context.bot.send_video_note(chat_id=update.effective_chat.id,
                                video_note=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_telegrambot_functions/base/example_video.mp4', 'rb'))


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_video_note))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()