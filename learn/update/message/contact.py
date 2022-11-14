from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, Contact


def contact(update, context):
    # for sending contact button ####1
    # context.bot.send_message(chat_id=update.message.chat_id, text=f"hi !!!",
    #                          reply_markup=ReplyKeyboardMarkup([[KeyboardButton(text="📲Contact", request_contact=True)]], resize_keyboard=True))

    update.message.reply_text(f"{update.message.contact}")
    # print(update.message.)

    # for send and foward contact message #####2
    # update.message.reply_contact(phone_number="12345678",
    #                              first_name="iqrorjon",
    #                              last_name="islomov")


    # for send and foward contact message #####3
    contact = Contact(phone_number="+998 90 360 5293",
                      first_name="Iqrorjon",
                      last_name="Islomov",
                      user_id=1035463819,
                      vcard="@IqrorjonCoder")
    update.message.reply_contact(contact=contact)


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', contact))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
