from telegram.ext import Updater, CommandHandler
from telegram import MenuButtonCommands, MenuButtonDefault


def setChatMenuButton(update, context):
    x = context.bot.setChatMenuButton(chat_id=update.effective_chat.id,
                                         menu_button=MenuButtonDefault())
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', setChatMenuButton))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()