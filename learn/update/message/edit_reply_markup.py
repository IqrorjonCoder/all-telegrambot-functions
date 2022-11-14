from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Location, InputMediaVideo


def edit_reply_markup(update, context):
    print(update.message.message_id)

    update.message.reply_text("salom", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("one", callback_data="123")]]))

    context.bot.edit_message_reply_markup(chat_id=update.message.chat_id,
                                          message_id=update.message.message_id-1,
                                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("two", callback_data="123")]]))


def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', edit_reply_markup))
    # dispatcher.add_handler(MessageHandler(Filters.video, edit_reply_markup))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print('ishga tushdi ...')
    runner()