import datetime
from telegram.ext import Updater, CommandHandler


def createChatInviteLink(update, context):
    link = context.bot.createChatInviteLink(chat_id=update.effective_chat.id, expire_date=datetime.datetime.today())

    update.message.reply_text(f"link is : \n*{link}*", parse_mode="Markdown")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', createChatInviteLink))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()