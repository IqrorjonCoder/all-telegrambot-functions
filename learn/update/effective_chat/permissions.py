from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatPermissions


def permissions(update, context):
    update.effective_chat.set_permissions(permissions=ChatPermissions(can_send_messages=True,
                                                                      can_send_media_messages=True,
                                                                      can_send_polls=True,
                                                                      can_send_other_messages=True,
                                                                      can_add_web_page_previews=True,
                                                                      can_change_info=True,
                                                                      can_invite_users=True,
                                                                      can_pin_messages=True, ))

    x = update.effective_chat.permissions
    update.message.reply_text(f"permissions : \n{x}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', permissions))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
