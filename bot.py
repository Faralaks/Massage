import sqlite3
from io import BytesIO

import telebot
from config import TELEGRAM_TOKEN, TRUSTED, DB_PATH
import os
from app import make_xlsx
bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    uid = message.from_user.id
    if uid in TRUSTED:
        base = open("./db/db.sqlite", "rb")
        bot.send_document(uid, caption="На Свою Базу!", data=base)
        base.close()

        stream = BytesIO()
        make_xlsx(stream, "cur")
        stream.name = "Отчет за текущий месяц.xlsx"
        bot.send_document(uid, caption="На За Текущий Месяц!", data=stream, disable_notification=True)
        del stream

        stream = BytesIO()
        make_xlsx(stream, 'prev')
        stream.name = "Отчет за предыдущий месяц.xlsx"
        bot.send_document(uid, caption="На За Предыдущий Месяц!", data=stream, disable_notification=True)

    else:
        bot.send_message(uid, "Ты чужой, почему твой UID = %d?"%uid)


def run():
    global trusted
    trusted = []
    if os.path.exists("trusted.txt"):
        trusted = open("trusted.txt", "r").readlines()
    trusted_file = open("trusted.txt", "w")
    print(' >>> Run Telegram bot')
    bot.polling()
