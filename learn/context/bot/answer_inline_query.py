from html import escape
from uuid import uuid4

from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, InlineQueryHandler, ConversationHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResult, InlineQuery, \
    InlineQueryResultArticle, InputTextMessageContent, ParseMode
from telegram.utils.helpers import escape_markdown

states = {
    "inline": 1,
}


def start(update, context):
    print(update.message.message_id)
    update.message.reply_text("select one of them ...")
    return states["inline"]


def answer_inline_query(update, context):
    print("salommmm")
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id="1",
            title="simple_text",
            input_message_content=InputTextMessageContent(f"simplelyfy : "),
        )
    ]

    update.inline_query.answer(results)
    # context.bot.answer_inline_query(inline_query_id=update.inline_query.id,
    #                                 results=results)
    # return ConversationHandler.END


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(ConversationHandler(
    #     entry_points=[CommandHandler('start', start)],
    #     states={
    #         1: [InlineQueryHandler(answer_inline_query, pattern="[a-z]")],
    #     },
    #     fallbacks=[CommandHandler('start', start)],
    #     per_chat=False,
    # ))
    InlineQueryHandler(answer_inline_query)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
