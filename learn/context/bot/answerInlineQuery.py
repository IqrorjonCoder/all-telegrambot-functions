from telegram.ext import Updater, InlineQueryHandler, MessageHandler, Filters
from telegram import InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultCachedAudio, \
    InputTextMessageContent


from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def answerInlineQuery(update, context):

    if update.inline_query.query == "article":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultArticle(
                                              id='1',
                                              title="simplee",
                                              input_message_content=InputTextMessageContent(f"article: *{update.inline_query.query}*\n\nthis is an simple text foir article !",parse_mode="Markdown"),
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("linkk",callback_data="linkk",url="https://kundalik.com")]]),
                                              thumb_url="https://cdn.pixabay.com/photo/2015/02/04/05/01/musician-623362__340.jpg",
                                              thumb_width=100,
                                              thumb_height=100,
                                              description="imagee"
                                          ),
                                      ]
                                      )

    elif update.inline_query.query == "audio":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultAudio(
                                              id='2 ',
                                              audio_url="https://samplelib.com/lib/preview/mp3/sample-3s.mp3",
                                              title="audio title",
                                              performer="audio performer",
                                              audio_duration=1,
                                              caption="*audio* simple and example captionn.",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("audio link", callback_data="link", url="https://samplelib.com/lib/preview/mp3/sample-3s.mp3")]]),
                                              thumb_url="https://cdn.pixabay.com/photo/2015/02/04/05/01/musician-623362__340.jpg",
                                              thumb_width=100,
                                              thumb_height=100,
                                              description="imagee",
                                              parse_mode="Markdown"
                                          )
                                      ])

    elif update.inline_query.query == "audio_cached":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultCachedAudio(
                                              id='3',
                                              audio_file_id="CQACAgIAAxkBAAIb_WOKGXw8FFbahUybvR3joZAe3uC3AAKKIgACFcNQSPpaVY1xkh7NKwQ",
                                              caption="cached audio filee.",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("music", callback_data="music!")]]),
                                              input_message_content=InputTextMessageContent("this is InputTextMessageContent example!")
                                          )
                                      ])



def runner():
    updater = Updater(token='5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(InlineQueryHandler(answerInlineQuery))
    # dispatcher.add_handler(MessageHandler(Filters.audio, answerInlineQuery))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

# {'file_unique_id': 'AgADiiIAAhXDUEg', 'file_name': 'mp3_example.mp3', 'performer': 'Kevin MacLeod', 'file_id': 'CQACAgIAAxkBAAIb_WOKGXw8FFbahUybvR3joZAe3uC3AAKKIgACFcNQSPpaVY1xkh7NKwQ', 'file_size': 764176, 'mime_type': 'audio/mpeg', 'duration': 27, 'title': 'Impact Moderato'}