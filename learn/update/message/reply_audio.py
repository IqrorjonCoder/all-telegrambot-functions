from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import Audio


def reply_audio(update, context):
    update.message.reply_text("salom ...")
    print(update.message.audio)
    # 1
    update.message.reply_audio(open('C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/mp3_example.mp3', 'rb'),
                               duration=999,
                               performer="performer",
                               title='this is title',
                               caption="this is caption text")
    # 2
    update.message.reply_audio(Audio(file_id="CQACAgIAAx0CX-u1ywACAtNjdIXLlnMwlnoORdwf-2do_YHp7QACNycAArcBoUsGaTKm2houUisE",
                                     file_unique_id="AgADNycAArcBoUs",
                                     duration=12346,
                                     performer="performer",
                                     title="title",
                                     file_size=9999,
                                     file_name="filename.mp3"))



def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(MessageHandler(Filters.audio, reply_audio))
    dispatcher.add_handler(CommandHandler('start', reply_audio))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()