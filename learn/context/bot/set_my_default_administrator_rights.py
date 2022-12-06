from telegram.ext import Updater, CommandHandler
from telegram import ChatAdministratorRights


def set_my_default_administrator_rights(update, context):
    x = context.bot.set_my_default_administrator_rights(rights=ChatAdministratorRights(is_anonymous=False,
                                                                                       can_manage_chat=True,
                                                                                       can_delete_messages=False,
                                                                                       can_manage_video_chats=False,
                                                                                       can_restrict_members=False,
                                                                                       can_change_info=True,
                                                                                       can_invite_users=True,
                                                                                       can_promote_members=False),
                                                        for_channels=False)
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_my_default_administrator_rights))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()