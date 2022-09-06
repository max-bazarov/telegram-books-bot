import os

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from books import get_all_books, add_book, delete_last_book

load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')


def delete_book(update, context):
    try:
        delete_last_book()
        update.message.reply_text('Последняя книга удалена')
    except Exception as e:
        update.message.reply_text(f'Ошибка: {e}')


def get_books(update, context):
    books = get_all_books()[1:]
    message = 'Список книг:\n\n' + '\n'.join(books)
    update.message.reply_text(message)


def new_book(update, context):
    try:
        book = update.message.text
        add_book(book)
        update.message.reply_text(f'Книга "{book}" добавлена')
    except Exception as e:
        update.message.reply_text(f'Ошибка: {e}')


def start(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup(
        [['/books', '/delete']],
        resize_keyboard=True
    )
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет! Я бот для учёта книг',
        reply_markup=buttons
    )


def main():
    updater = Updater(token=token)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(
        CommandHandler('books', get_books)
    )
    updater.dispatcher.add_handler(
        CommandHandler('delete', delete_book)
    )
    updater.dispatcher.add_handler(MessageHandler(Filters.text, new_book))

    updater.start_polling()


if __name__ == '__main__':
    main()
