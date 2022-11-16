from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import Document


def reply_document(update, context):

    # print(update.message.document)

    # 1
    update.message.reply_document(document=Document(file_id="BQACAgIAAxkBAAIYRmN0jJAZEu0e-24DnuVJ69oouYVMAAJFIwACHvipSxHkEdoeYJq8KwQ",
                                                    file_unique_id="AgADRSMAAh74qUs",
                                                    file_name="axample.py",
                                                    file_size=1245))

    # 2
    update.message.reply_document(document=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/example.py', 'rb'),
                                  filename="an example file.py",
                                  caption="this is captiuon text",
                                  quote=True,
                                  thumb=open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/gif_example.mp4', 'rb'))


def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(MessageHandler(Filters.document, reply_document))
    dispatcher.add_handler(CommandHandler('start', reply_document))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()