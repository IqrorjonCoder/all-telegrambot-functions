from telegram.ext import Updater, Filters, MessageHandler
from telegram import ParseMode


def caption_markdown(update, context):
    update.message.reply_text(f"caption markdown : \n\n {update.message.caption_markdown}")
    print(update.message.caption_markdown)

    # for coping and resending
    # update.message.reply_animation(animation=open("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/gif_example.mp4", 'rb'),
    #                                caption="<a href='https://kundalik.com'>this</a> is simple caption <b>text</b>",
    #                                parse_mode=ParseMode.HTML)


def runner():
    updater = Updater(token="5693888427:AAFE-_nYnUSOxtgDu-hXprZgUvyrLxS_KTE")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.animation, caption_markdown))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishlamoqda ...")
    runner()