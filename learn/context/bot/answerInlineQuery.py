from telegram.ext import Updater, InlineQueryHandler, MessageHandler, Filters
from telegram import InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultCachedAudio, \
    InlineQueryResultCachedDocument, InlineQueryResultCachedGif, \
    InlineQueryResultCachedMpeg4Gif, InlineQueryResultCachedPhoto, InlineQueryResultCachedSticker, \
    InlineQueryResultCachedVideo, InlineQueryResultCachedVoice, InlineQueryResultContact, InlineQueryResultDocument,\
    InlineQueryResultGame, InlineQueryResultGif, InlineQueryResultLocation, InlineQueryResultMpeg4Gif, \
    InlineQueryResultPhoto, InlineQueryResultVenue, InlineQueryResultVideo, InlineQueryResultVoice, \
    InputContactMessageContent, InputInvoiceMessageContent, InputLocationMessageContent, InputTextMessageContent, \
    InputVenueMessageContent, InputMessageContent

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, LabeledPrice


def answerInlineQuery(update, context):
    # print(update.message.audio)
    # print(update.message.document)
    # print(update.message.animation)
    # print(update.message.photo[-1])
    # print(update.message.sticker)
    # print(update.message.video)
    # print(update.message.voice)

    if update.inline_query.query == "none":
        print("Noneee")


    elif update.inline_query.query == "article":
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
                                              id='1',
                                              audio_file_id="CQACAgIAAxkBAAIcC2OK0MfncHzEU-jZX6JQnaiVHFbUAAKlIgACc8xYSBVw7QMAATcu5isE",
                                              caption="cached audio filee.",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("music", callback_data="music!")]]),
                                          )
                                      ])


    elif update.inline_query.query == "document_cached":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultCachedDocument(
                                              id='1',
                                              title="title of the documentt",
                                              document_file_id="BQACAgIAAxkBAAIcGWOK09JEiecs5tjbCsSYtb3Hjv75AAKrIgACc8xYSGP_4ij8gOZAKwQ",
                                              description="description of the file",
                                              caption="caption of the document file.",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("document", callback_data="document")]])
                                          )
                                      ])

    elif update.inline_query.query == "gif_cached":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultCachedGif(
                                              id='1',
                                              gif_file_id="CgACAgIAAxkBAAIcI2OK2DU-taEVZwABnrqYiNtlB7FkbQACzw8AAgThSEjcqJCYh9KoGCsE",
                                              title="title of the gif",
                                              caption="caption of the gif",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("gif", callback_data="gif")]]),
                                          )
                                      ])

    elif update.inline_query.query == "mpeg4gif_cached":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultCachedMpeg4Gif(
                                              id='1',
                                              mpeg4_file_id="CgACAgIAAxkBAAIcJGOK2WvHhqhbc4KPgUNMiHhFTgnOAAK5IgACc8xYSNPwmnNb6Hy-KwQ",
                                              title="title of the mpeg4 gif",
                                              caption="caption of the mpeg4 gif",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("mpeg4 gif", callback_data="mpeg4 gif")]]),
                                          )
                                      ])

    elif update.inline_query.query == "photo_cached":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultCachedPhoto(
                                              id='1',
                                              photo_file_id="AgACAgIAAxkBAAIcKGOK2yQxrQz7gPRd5HVljl_oaDWJAAKNwzEbc8xYSKzcOlDXrWLwAQADAgADeAADKwQ",
                                              title="title of the photo",
                                              description="description of the photo",
                                              caption="caption of the photo file",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("photo", callback_data="photo")]])
                                          )
                                      ])

    elif update.inline_query.query == "sticker_cached":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultCachedSticker(
                                              id='1',
                                              sticker_file_id="CAACAgIAAxkBAAIcLGOK29OFmjJ7PimGONgdEhExoZdvAALCIgACc8xYSL9NVFKwyj0TKwQ",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("sticker", callback_data="sticker")]])
                                          )
                                      ])

    elif update.inline_query.query == "video_cached":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultCachedVideo(
                                              id='1',
                                              video_file_id="BAACAgIAAxkBAAIcLmOK3VMQV57uOPH-O7D7IDwXW3iTAALMIgACc8xYSLkslGBMr-YJKwQ",
                                              title="title of the video",
                                              description="description of the video",
                                              caption="caption of the video",
                                              reply_markup=InlineKeyboardMarkup(
                                                  [[InlineKeyboardButton("video", callback_data="video")]])
                                          )
                                      ])

    elif update.inline_query.query == "voice_cached":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultCachedVoice(
                                              id='1',
                                              voice_file_id='AwACAgIAAxkBAAIcMGOK3j0S2NROm6diJInjO36WXshYAALOIgACc8xYSFKbNUhQ2RXUKwQ',
                                              title='title of the voice',
                                              caption="caption of the voice",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("voice", callback_data="voice")]])
                                          )
                                      ])


    elif update.inline_query.query == "contact":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultContact(
                                              id='1',
                                              phone_number="+998 90 627 03 91",
                                              first_name="first namee",
                                              last_name="last namee",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("contact", callback_data="contact")]])
                                          )
                                      ])

    elif update.inline_query.query == "document":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultDocument(
                                              id='1',
                                              document_url="https://www.africau.edu/images/default/sample.pdf",
                                              mime_type="application/pdf",
                                              title="title of the document",
                                              caption="caption of the document",
                                              description="description of the document",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("document url", callback_data="document url", url="https://www.africau.edu/images/default/sample.pdf")]])
                                          )
                                      ])

    elif update.inline_query.query == "game":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultGame(
                                              id='1',
                                              game_short_name="@gamee LittlePlane",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("game", callback_data="game")]])
                                          )
                                      ])


    elif update.inline_query.query == "gif":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultGif(
                                              id='1',
                                              gif_url="https://media.wired.com/photos/5b4502213f4d850b4f4c1726/master/w_1600%2Cc_limit/Boglio_05.gif",
                                              thumb_url="https://media.wired.com/photos/5b4502213f4d850b4f4c1726/master/w_1600%2Cc_limit/Boglio_05.gif",
                                              title="title of the gif file",
                                              caption="caption of the gif file",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("gif", callback_data="gif", url="https://media.wired.com/photos/5b4502213f4d850b4f4c1726/master/w_1600%2Cc_limit/Boglio_05.gif")]])
                                          )
                                      ])


    elif update.inline_query.query == "location":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultLocation(
                                              id='1',
                                              latitude=41.291413,
                                              longitude=69.278435,
                                              title="title of the location",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("location", callback_data="location", url="https://www.google.com/maps/place/Astrum+-+IT+Academy/@41.3155483,69.4509227,29849m/data=!3m1!1e3!4m5!3m4!1s0x38ae5774bb568c81:0x5a794f7263a1e89a!8m2!3d41.3135419!4d69.5283904")]])
                                          )
                                      ])

    elif update.inline_query.query == "mpeg4gif":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultMpeg4Gif(
                                              id='1',
                                              mpeg4_url="https://media2.giphy.com/media/hv4yp9UoVyil8IujGW/giphy.gif?cid=ecf05e47dnmystqtghiec1emzw2al9zu7yf5d34r2b5cxzi0&rid=giphy.gif&ct=g",
                                              thumb_url="https://media2.giphy.com/media/hv4yp9UoVyil8IujGW/giphy.gif?cid=ecf05e47dnmystqtghiec1emzw2al9zu7yf5d34r2b5cxzi0&rid=giphy.gif&ct=g",
                                              title="title of the mpeg4gif",
                                              caption="caption of the mprg4gif",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("gif", callback_data="gif", url="https://media2.giphy.com/media/hv4yp9UoVyil8IujGW/giphy.gif?cid=ecf05e47dnmystqtghiec1emzw2al9zu7yf5d34r2b5cxzi0&rid=giphy.gif&ct=g")]])
                                          )
                                      ])


    elif update.inline_query.query == "photo":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultPhoto(
                                              id='1',
                                              photo_url="https://cdn.pixabay.com/photo/2015/02/04/05/01/musician-623362__340.jpg",
                                              thumb_url="https://cdn.pixabay.com/photo/2015/02/04/05/01/musician-623362__340.jpg",
                                              title="title of the photo",
                                              description="description of the photo",
                                              caption="caption of the photo",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("photo", url="https://cdn.pixabay.com/photo/2015/02/04/05/01/musician-623362__340.jpg", callback_data="photo")]])
                                          )
                                      ])


    elif update.inline_query.query == "venue":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultVenue(
                                              id='1',
                                              latitude=41.291413,
                                              longitude=69.278435,
                                              title='title of the venue',
                                              address="address of the venue",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("venue", url="https://www.google.com/maps/place/Astrum+-+IT+Academy/@41.3155483,69.4509227,29849m/data=!3m1!1e3!4m5!3m4!1s0x38ae5774bb568c81:0x5a794f7263a1e89a!8m2!3d41.3135419!4d69.5283904", callback_data="venue")]])
                                          )
                                      ])


    elif update.inline_query.query == "video":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultVideo(
                                              id='1',
                                              video_url="https://media.istockphoto.com/id/1402376759/video/hand-drawn-tangle-scrawl-sketch-line-like-finding-a-solution-abstract-scribble-shape.mp4?s=mp4-640x640-is&k=20&c=uUX6KlfP_FzI62Rx7x5xwuW-TodKtW55u75j1DQ4nVM=",
                                              mime_type="video/mp4",
                                              thumb_url="https://media.istockphoto.com/id/1402376759/video/hand-drawn-tangle-scrawl-sketch-line-like-finding-a-solution-abstract-scribble-shape.mp4?s=mp4-640x640-is&k=20&c=uUX6KlfP_FzI62Rx7x5xwuW-TodKtW55u75j1DQ4nVM=",
                                              title="title of the video",
                                              caption="caption of the video",
                                              description="description of the video",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("video", url="https://media.istockphoto.com/id/1402376759/video/hand-drawn-tangle-scrawl-sketch-line-like-finding-a-solution-abstract-scribble-shape.mp4?s=mp4-640x640-is&k=20&c=uUX6KlfP_FzI62Rx7x5xwuW-TodKtW55u75j1DQ4nVM=", callback_data="video")]])
                                          )
                                      ])


    elif update.inline_query.query == "voice":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultVoice(
                                              id='1',
                                              voice_url="https://filesamples.com/samples/audio/ogg/Symphony%20No.6%20(1st%20movement).ogg",
                                              title="title of the voice",
                                              caption="caption of the voice",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("voice", url="https://filesamples.com/samples/audio/ogg/Symphony%20No.6%20(1st%20movement).ogg", callback_data="voice")]])
                                          )
                                      ])


    elif update.inline_query.query == "contact_content":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultArticle(
                                              id='1',
                                              title='title of the contact content',
                                              input_message_content=InputContactMessageContent(phone_number="+998 90 627 03 91",first_name="first namee",last_name="last namee"),
                                              description="description of the contact content",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("sendd", url="https://kundalik.com", callback_data="sendd")]])
                                          ),
                                      ])


    elif update.inline_query.query == "invoice_content":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultArticle(
                                              id='1',
                                              title='title of the invoice content',
                                              input_message_content=InputInvoiceMessageContent(
                                                  title="simple payment for example",
                                                  description="description of the payment for example",
                                                  payload="simple",
                                                  provider_token="398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065",
                                                  currency="uzs",
                                                  prices=[LabeledPrice(label="100 $", amount=100000)],
                                                  photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRy5tDW-tz8BUWwWcKuVeXJZHDyEYKPboMtaUl1jj4l&s"
                                              ),
                                              description="description of the contact content",
                                          ),
                                      ])



    elif update.inline_query.query == "location_content":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultArticle(
                                              id='1',
                                              title='title of the invoice content',
                                              input_message_content=InputLocationMessageContent(latitude=12.123, longitude=13.123),
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("let's go", url="https://www.google.com/maps/place/Astrum+-+IT+Academy/@41.3155483,69.4509227,29849m/data=!3m1!1e3!4m5!3m4!1s0x38ae5774bb568c81:0x5a794f7263a1e89a!8m2!3d41.3135419!4d69.5283904", callback_data="go")]]),
                                              description="description of the locationn"
                                          ),
                                      ])


    elif update.inline_query.query == "venue_content":
        context.bot.answerInlineQuery(inline_query_id=str(update.inline_query.id),
                                      results=[
                                          InlineQueryResultArticle(
                                              id='1',
                                              title='title of the venue content',
                                              input_message_content=InputVenueMessageContent(
                                                  latitude=12.123,
                                                  longitude=13.123,
                                                  title="Astrum IT Academy",
                                                  address="Tashkent, Uzbekistan"
                                              ),
                                              description="description of the venue content",
                                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("venue", callback_data="venue", url="https://www.google.com/maps/place/Astrum+-+IT+Academy/@41.3155483,69.4509227,29849m/data=!3m1!1e3!4m5!3m4!1s0x38ae5774bb568c81:0x5a794f7263a1e89a!8m2!3d41.3135419!4d69.5283904")]])
                                          ),
                                      ])






def runner():
    updater = Updater(token='5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(InlineQueryHandler(answerInlineQuery))

    # dispatcher.add_handler(MessageHandler(Filters.audio, answerInlineQuery))
    # dispatcher.add_handler(MessageHandler(Filters.document, answerInlineQuery))
    # dispatcher.add_handler(MessageHandler(Filters.animation, answerInlineQuery))
    # dispatcher.add_handler(MessageHandler(Filters.photo, answerInlineQuery))
    # dispatcher.add_handler(MessageHandler(Filters.sticker, answerInlineQuery))
    # dispatcher.add_handler(MessageHandler(Filters.video, answerInlineQuery))
    # dispatcher.add_handler(MessageHandler(Filters.voice, answerInlineQuery))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()