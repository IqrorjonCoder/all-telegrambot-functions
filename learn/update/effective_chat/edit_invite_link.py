import datetime

from telegram.ext import Updater, CommandHandler


def edit_invite_link(update, context):
    update.message.reply_text(f"""edit_invite_link : \n{update.effective_chat.edit_invite_link(invite_link="https://t.me/+84xVSc75dy1iMDli", expire_date=datetime.datetime.now(), member_limit=11)}""")




def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', edit_invite_link))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()