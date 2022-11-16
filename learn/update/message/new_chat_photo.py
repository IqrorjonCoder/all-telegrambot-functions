from telegram.ext import Updater, MessageHandler, Filters
import wget


def new_chat_photo(update, context):
    update.message.reply_text(f"your uploaded chat image \n\nimage ... \n {update.message.new_chat_photo[-1]}")
    x = context.bot.get_file(update.message.new_chat_photo[-1]['file_id'])
    wget.download(url=f"{x['file_path']}",
                  out=f"C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/{x['file_unique_id']}.jpg")
    update.message.reply_photo(open(f"C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/{x['file_unique_id']}.jpg", 'rb'))


def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_photo, new_chat_photo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()