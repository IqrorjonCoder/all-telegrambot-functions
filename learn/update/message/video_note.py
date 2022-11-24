from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import VideoNote


def video_note(update, context):
    v_note = VideoNote(file_id="AAMCAgADGQEAAhkqY39s_dN1sAVVSQza951o011t2PUAAjghAALp7gABSMOa6CM_mzUdAQAHbQADKwQ",
                       file_unique_id="AQADOCEAAunuAAFIcg",
                       length=384,
                       duration=21)
    update.message.reply_video_note(video_note=v_note)



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, video_note))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

# {'length': 384, 'thumb': {'height': 320, 'width': 320, 'file_unique_id': 'AQADOCEAAunuAAFIcg', 'file_id': 'AAMCAgADGQEAAhkqY39s_dN1sAVVSQza951o011t2PUAAjghAALp7gABSMOa6CM_mzUdAQAHbQADKwQ', 'file_size': 21830}, 'file_unique_id': 'AgADOCEAAunuAAFI', 'duration': 21, 'file_id': 'DQACAgIAAxkBAAIZKmN_bP3TdbAFVUkM2vedaNNdbdj1AAI4IQAC6e4AAUjDmugjP5s1HSsE', 'file_size': 2893848}
