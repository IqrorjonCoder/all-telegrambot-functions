from telegram.ext import Updater, MessageHandler, Filters


def get_game_high_scores(update, context):
    update.message.reply_text("salom ...")
    print(update.message.from_user)
    print(update.message.message_id)
    # 609
    # update.message.get_game_high_scores(user_id=1035463819)
    context.bot.get_game_high_scores(chat_id=update.message.chat_id,
                                     message_id=613,
                                     user_id=1035463819)



def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.game, get_game_high_scores))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()