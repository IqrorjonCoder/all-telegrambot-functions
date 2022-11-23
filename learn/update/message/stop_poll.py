from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def stop_poll(update, context):
    print(update.message.poll)
    print(update.message.message_id)

    update.message.stop_poll(reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("xxx", callback_data="iqrorjon")]]))

    context.bot.stop_poll(chat_id=update.message.chat_id,
                          message_id=update.message.message_id,
                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("xxx", callback_data="iqrorjon")]]))

def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', stop_poll))
    dispatcher.add_handler(MessageHandler(Filters.poll, stop_poll))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

# {'total_voter_count': 0, 'explanation_entities': [], 'id': '5472045685249409988', 'options': [{'text': 'iqrorjon', 'voter_count': 0}, {'text': 'humoyun', 'voter_count': 0}, {'text': 'azamat', 'voter_count': 0}], 'is_closed': False, 'question': 'what is your name?', 'allows_multiple_answers': False, 'correct_option_id': 0, 'type': 'quiz', 'is_anonymous': False, 'close_date': None}
# 6375
