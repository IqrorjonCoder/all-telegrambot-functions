from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import Game, PhotoSize


def reply_game(update, context):
    print(update.message.game)

    game = Game(title="iqrorjon gamee",
                description="this is an exmple gamee",
                photo=PhotoSize(file_id="AQADs7sxG3cEaVJ4",
                                file_unique_id="AgACAgQAAxUAAWN0jmlVhZsv0nenqw5TbFUC8RorAAKzuzEbdwRpUucaI7KdUS_8AQADAgADcwADKwQ",
                                width=1,
                                height=1))

    update.message.reply_game(game_short_name="game")
    # context.bot.send_game()

def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(MessageHandler(Filters.game, reply_game))
    dispatcher.add_handler(CommandHandler('start', reply_game))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()