from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton, Location, InputMediaVideo


def edit_media(update, context):
    print(update.message.message_id)
    # update.message.edit_media()

    context.bot.edit_message_media(chat_id=update.message.chat_id,
                                   message_id=469,
                                   media=InputMediaVideo(media=open("C:/Users/student.ASTRUM-DOMAIN/Downloads/video5424780832877321625.mp4"), caption="this is media!"))




def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', edit_media))
    # dispatcher.add_handler(MessageHandler(Filters.video, edit_media))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print('ishga tushdi ...')
    runner()