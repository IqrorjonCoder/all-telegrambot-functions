import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown

# Включение ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
# создаем `logger` с именем файла
logger = logging.getLogger(__name__)


# Определяем несколько обработчиков команд.
# Они обычно принимают два аргумента `update` и `context`.
# Обработчики ошибок также получают исключения `TelegramError`.
# т.к. аргумент `context` в обработчиках не используется и
# во избежании путаницы заменим его на переменную `_`
def start(update, _):
    """Сообщение при команде `/start`"""
    update.message.reply_text('Привет!')


def help_command(update, _):
    """Сообщение при команде `/help`."""
    update.message.reply_text('Введите: @логин_бота и через пробел какое либо сообщение.')


def inlinequery(update, _):
    """Обработка встроенного запроса."""
    # извлекаем текст сообщения
    query = update.inline_query.query
    # формируем результат в зависимости от того
    # что выберет пользователь из так называемого
    # меню `title`.
    results = [
        # Аргумент `id` служит для извлечения выбранного из `title` результата
        #  преобразования, в `id` так же можно использовать строку,
        # используемую в `title`, если конечно она уникальная
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="UPPER",
            input_message_content=InputTextMessageContent(query.upper()),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="BOLD",
            input_message_content=InputTextMessageContent(
                f"*{escape_markdown(query)}*", parse_mode=ParseMode.MARKDOWN
            ),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="ITALIC",
            input_message_content=InputTextMessageContent(
                f"_{escape_markdown(query)}_", parse_mode=ParseMode.MARKDOWN
            ),
        ),
    ]
    # отвечаем на сообщение результатом
    _.bot.answer_inline_query(inline_query_id=update.inline_query.id, results=results)


if __name__ == '__main__':
    # Создаем Updater с токеном вашего бота.
    updater = Updater("5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")

    # Получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # отвечаем на команды Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # на простые сообщения отвечаем тем же сообщением,
    # только преобразуем текст в зависимости от
    # выбранного `title` - UPPER, BOLD, ITALIC
    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    # Старт бота
    updater.start_polling()
    updater.idle()
