from telegram.ext import Updater, MessageHandler, Filters


def new_chat_members(update, context):
    print(update.message.new_chat_members[0].to_dict())
    account_data = update.message.new_chat_members[0].to_dict()

    update.message.reply_text(
        f"Assalomu alaykum {account_data['last_name']}.{account_data['first_name']}! Bizning guruhimizga xush kelibsiz!, \n[*{account_data['last_name']}.{account_data['first_name']}*](tg://user?id={account_data['id']})",
        parse_mode="Markdown")

def runner():
    updater = Updater(token="XXXXXXXXXXXX")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_chat_members))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
