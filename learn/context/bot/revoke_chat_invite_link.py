import datetime
from telegram.ext import Updater, CommandHandler


def revoke_chat_invite_link(update, context):
    x0 = context.bot.create_chat_invite_link(chat_id=update.effective_chat.id,
                                             expire_date=datetime.datetime.today(),
                                             name="simplee_linkk")

    update.message.reply_text(f"created : {x0}")

    x = context.bot.revoke_chat_invite_link(chat_id=update.effective_chat.id,
                                            invite_link=f"{x0.invite_link}")
    update.message.reply_text(f"revoke_chat_invite_link : {x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', revoke_chat_invite_link))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()