from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import Audio


got_data = {
    "caption_entities": [],
    "date": 1668247937,
    "new_chat_members": [],
    "new_chat_photo": [],
    "chat": {
        "last_name": "Islomov",
        "first_name": "Iqrorjon",
        "id": 1035463819,
        "type": "private",
        "username": "IqrorjonCoder"
    },
    "message_id": 124,
    "group_chat_created": False,
    "delete_chat_photo": False,
    "supergroup_chat_created": False,
    "entities": [],
    "audio": {
        "performer": "Kevin MacLeod",
        "file_id": "CQACAgIAAxkBAAN8Y29xgQ9-VWGZtyDfmmEi1DK2FEAAAjQhAAKzOnlL6HvLv5-pKR8rBA",
        "file_name": "mp3_example.mp3",
        "title": "Impact Moderato",
        "duration": 27,
        "file_size": 764176,
        "mime_type": "audio/mpeg",
        "file_unique_id": "AgADNCEAArM6eUs"
    },
    "channel_chat_created": False,
    "photo": [],
    "from": {
        "last_name": "Islomov",
        "language_code": "en",
        "id": 1035463819,
        "is_bot": False,
        "first_name": "Iqrorjon",
        "username": "IqrorjonCoder"
    }
}


def audio(update, context):

    x = Audio(file_id="CQACAgIAAxkBAAN8Y29xgQ9-VWGZtyDfmmEi1DK2FEAAAjQhAAKzOnlL6HvLv5-pKR8rBA",
              file_unique_id="AgADNCEAArM6eUs",
              duration=1,
              performer="IqrorjonCoder audio artit",
              title="this is title",
              file_size=1)

    # 1
    update.message.reply_audio(audio=x)


    # 2
    update.message.reply_audio(audio=open("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/mp3_example.mp3", 'rb'),
                               duration=1,
                               performer="IqrorjonCoder audio artit",
                               title="this is title",
                               filename="filename_ex")


def runner():
    updater = Updater(token="5693888427:AAFE-_nYnUSOxtgDu-hXprZgUvyrLxS_KTE")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', audio))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishlamoqda ...")
    runner()