import Constants as keys
from telegram.ext import *
import Convertor as R
#импортируем нужные нам библиотеки и файфцлы
print("Привет, пользователь!Я Xakaton.BOT, и я могу конвертировать файлы формата .frx в формат.pdf Что я умею: /start - начать работу /help - помощь /status - Статус обработки файлов")

#функции для работы бота
def start_command(update, context):
    update.message.reply_text('Введи что то чтоб начать!')


def help_start_command(update, context):
    update.message.reply_text('Если тебе нужна помощь просто напиши: Какие у тебя есть команды?')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, contex):
    print(f"Update {update} caused error {contex.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_start_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
#вызов различных функций для работы программы

main()
