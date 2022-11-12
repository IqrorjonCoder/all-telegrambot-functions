from telegram.ext import Updater, CommandHandler
from telegram import Animation

got_data = {
    "update_id": 812088497,
    "message": {
        "message_id": 103,
                "chat": {
                    "first_name": "Iqrorjon",
                         "type": "private",
                         "username": "IqrorjonCoder",
                         "id": 1035463819,
                         "last_name": "Islomov"
                },
                "entities": [],
                "new_chat_members": [],
                "document": {
                    "file_id": "CgACAgIAAxkBAANnY29tLaaSMtHby80d9PGI0jTUUF8AAh4hAAKzOnlLHPK4EDz-0VkrBA",
                             "file_unique_id": "AgADHiEAArM6eUs",
                             "file_name": "Scary3.mp4",
                             "mime_type": "video/mp4",
                             "file_size": 265864,
                             "thumb": {
                                 "file_id": "AAMCAgADGQEAA2djb20tppIy0dvLzR308YjSNNRQXwACHiEAArM6eUsc8rgQPP7RWQEAB20AAysE",
                                       "file_unique_id": "AQADHiEAArM6eUty",
                                       "file_size": 8678,
                                       "height": 240,
                                       "width": 320
                             }
                },
                "delete_chat_photo": False,
                "channel_chat_created": False,
                "supergroup_chat_created": False,
                "date": 1668246830,
                "animation": {
                    "duration": 1,
                              "file_id": "CgACAgIAAxkBAANnY29tLaaSMtHby80d9PGI0jTUUF8AAh4hAAKzOnlLHPK4EDz-0VkrBA",
                              "file_unique_id": "AgADHiEAArM6eUs",
                              "file_name": "Scary3.mp4",
                              "mime_type": "video/mp4",
                              "file_size": 265864,
                              "height": 960,
                              "width": 1280,
                              "thumb": {
                                  "file_id": "AAMCAgADGQEAA2djb20tppIy0dvLzR308YjSNNRQXwACHiEAArM6eUsc8rgQPP7RWQEAB20AAysE",
                                        "file_unique_id": "AQADHiEAArM6eUty",
                                        "file_size": 8678,
                                        "height": 240,
                                        "width": 320
                              }
                },
                "group_chat_created": False,
                "caption_entities": [],
                "photo": [],
                "new_chat_photo": [],
                "from": {
                    "first_name": "Iqrorjon",
                         "username": "IqrorjonCoder",
                         "last_name": "Islomov",
                         "id": 1035463819,
                         "language_code": "en",
                         "is_bot": False
                }
    }
}


def animation(update, context):
    update.message.reply_text("salomm")

    # 1
    x = Animation(file_id="CgACAgIAAxkBAANnY29tLaaSMtHby80d9PGI0jTUUF8AAh4hAAKzOnlLHPK4EDz-0VkrBA",
                  file_unique_id="AgADHiEAArM6eUs",
                  width=320,
                  height=240,
                  duration=100,
                  file_name="simple animation")
    update.message.reply_animation(animation=x)


    # 2
    update.message.reply_animation(animation=open("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/gif_example.mp4", 'rb'),
                                   duration=1,
                                   caption="this is an example animation !")


def runner():
    updater = Updater(token='5693888427:AAFE-_nYnUSOxtgDu-hXprZgUvyrLxS_KTE')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', animation))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishlamoqda ...")
    runner()