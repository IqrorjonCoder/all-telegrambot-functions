import datetime
from telegram.ext import Updater, CommandHandler


def edit_chat_invite_link(update, context):
    new_link = context.bot.create_chat_invite_link(chat_id=update.effective_chat.id,
                                                   expire_date=datetime.datetime.today(),
                                                   name="simple_link_neww")

    update.message.reply_text(f"created link : {new_link}")

    x = context.bot.edit_chat_invite_link(chat_id=update.effective_chat.id,
                                          invite_link=f"{new_link.invite_link}",
                                          expire_date=datetime.datetime.today(),
                                          member_limit=20,
                                          name="second editted")
    update.message.reply_text(f"editted : {x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', edit_chat_invite_link))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()