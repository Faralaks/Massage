import time
from io import BytesIO
import telebot
from config import TELEGRAM_TOKEN, TRUSTED, DB_PATH, AUTO_DB_SEND_PERIOD, AUTO_SEND_RECIPIENT, AUTO_CUR_XL_SEND_PERIOD, AUTO_PREV_XL_SEND_PERIOD
from app import make_xlsx
bot = telebot.TeleBot(TELEGRAM_TOKEN)


def send_cur_xl(uid):
    stream = BytesIO()
    make_xlsx(stream, "cur")
    stream.name = "Отчет за текущий месяц.xlsx"
    bot.send_document(uid, caption="На За Текущий Месяц!", data=stream, disable_notification=True)


def send_prev_xl(uid):
    stream = BytesIO()
    make_xlsx(stream, 'prev')
    stream.name = "Отчет за предыдущий месяц.xlsx"
    bot.send_document(uid, caption="На За Предыдущий Месяц!", data=stream, disable_notification=True)


def send_db(uid):
    base = open("./db/db.sqlite", "rb")
    bot.send_document(uid, caption="На Свою Базу!", data=base)
    base.close()


def send_files(uid):
    send_cur_xl(uid)
    send_prev_xl(uid)
    send_db(uid)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    uid = message.from_user.id
    if uid in TRUSTED:
        send_files(uid)
    else:
        bot.send_message(uid, "Ты чужой, почему твой UID = %d?"%uid)


def db_auto_sender():
    print(' >>> Run Telegram bot db_auto_sender')
    while True:
        for uid in AUTO_SEND_RECIPIENT:
            send_db(uid)
        time.sleep(AUTO_DB_SEND_PERIOD)

def cur_xl_auto_sender():
    print(' >>> Run Telegram bot cur_xl_auto_sender')
    while True:
        for uid in AUTO_SEND_RECIPIENT:
            send_cur_xl(uid)
        time.sleep(AUTO_CUR_XL_SEND_PERIOD)


def prev_xl_auto_sender():
    print(' >>> Run Telegram bot prev_xl_auto_sender')
    while True:
        for uid in AUTO_SEND_RECIPIENT:
            send_prev_xl(uid)
        time.sleep(AUTO_PREV_XL_SEND_PERIOD)




def run():
    print(' >>> Run Telegram bot listener')
    bot.polling()
