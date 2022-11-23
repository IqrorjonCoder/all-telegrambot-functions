from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def set_game_score(update, context):
    print(update.message.from_user.id, update.message.message_id)
    # print(update.message.set_game_score())
    context.bot.set_game_score(chat_id=update.message.chat_id,
                               message_id=765,
                               user_id=1087968824,
                               score=100)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_game_score))
    # dispatcher.add_handler(MessageHandler(Filters.game, set_game_score))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

# data = {'animation': {'file_id': 'CgACAgQAAxUAAWN-PWBErLtfR9p6OH6WmxbFCdqYAAJBBgAChTkAAVAbkDbQw8u23SsE',
#                       'file_size': 355400,
#                       'file_unique_id': 'AgADQQYAAoU5AAFQ',
#                       'mime_type': 'video/mp4',
#                       'width': 320,
#                       'height': 180,
#                       'file_name': 'video.mp4',
#                       'duration': 5,
#                       'thumb': {'file_id': 'AAMCBAADFQABY349YESsu19H2no4fpabFsUJ2pgAAkEGAAKFOQABUBuQNtDDy7bdAQAHbQADKwQ',
#                                 'file_size': 11378,
#                                 'file_unique_id': 'AQADQQYAAoU5AAFQcg',
#                                 'width': 320,
#                                 'height': 180}},
#         'text_entities': [],
#         'photo': [{'file_id': 'AgACAgQAAxUAAWN-PWCPIpyZMGSYSpmFFfwlfbbjAALorzEbhTkAAVA5aHtFOk5CEQEAAwIAA3MAAysE',
#                    'file_size': 1118,
#                    'file_unique_id': 'AQAD6K8xG4U5AAFQeA',
#                    'width': 90,
#                    'height': 51},
#                   {'file_id': 'AgACAgQAAxUAAWN-PWCPIpyZMGSYSpmFFfwlfbbjAALorzEbhTkAAVA5aHtFOk5CEQEAAwIAA20AAysE',
#                    'file_size': 10209,
#                    'file_unique_id': 'AQAD6K8xG4U5AAFQcg',
#                    'width': 320,
#                    'height': 180},
#                   {'file_id': 'AgACAgQAAxUAAWN-PWCPIpyZMGSYSpmFFfwlfbbjAALorzEbhTkAAVA5aHtFOk5CEQEAAwIAA3gAAysE',
#                    'file_size': 27067,
#                    'file_unique_id': 'AQAD6K8xG4U5AAFQfQ',
#                    'width': 640,
#                    'height': 360}],
#         'title': 'Smartup Shark',
#         'description': 'Become the biggest fish in the ocean and eat them all!'}
