from telegram.ext import Updater, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent


def answer_inline_query(update, context):
    print(update)
    context.bot.answer_inline_query(inline_query_id=str(update.inline_query.id),
                                  results=[
                                      InlineQueryResultArticle(
                                          id='1',
                                          title="simplee",
                                          input_message_content=InputTextMessageContent("this is an simple text foir article !")
                                      ),
                                  ])


def runner():
    updater = Updater(token='5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(InlineQueryHandler(answer_inline_query))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()