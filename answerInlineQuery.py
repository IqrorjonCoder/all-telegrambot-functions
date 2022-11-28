from telegram.ext import Updater, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton


def answerInlineQuery(update, context):
    print(update)
    context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                  results=[
                                      InlineQueryResultArticle(
                                          id='1',
                                          title="simplee",
                                          input_message_content=InputTextMessageContent("this is an simple text foir article !"),
                                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("oneee")]])
                                      ),
                                  ])


def runner():
    updater = Updater(token='5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(InlineQueryHandler(answerInlineQuery))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()