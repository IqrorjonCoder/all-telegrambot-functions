from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import Animation


def reply_animation(update, context):
    update.message.reply_text("salom ...")
    print(update.message.animation)
    update.message.reply_animation(Animation(file_id="CgACAgIAAx0CX-u1ywACAsJjdIRp5unN9uBFvUiIRVwBZota6AACMScAArcBoUuxC0xOsVLnNSsE",
                                             file_unique_id="AgADMScAArcBoUs",
                                             duration=12345,
                                             width=1,
                                             height=1))



def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(MessageHandler(Filters.animation, reply_animation))
    dispatcher.add_handler(CommandHandler('start', reply_animation))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()