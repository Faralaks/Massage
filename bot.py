import telebot
from config import TELEGRAM_TOKEN, TRUSTED
import os
bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    uid = message.from_user.id
    if uid in TRUSTED:
        bot.send_message(uid, "На свою базу!")
    else:
        bot.send_message(uid, "Ты чужой или ввел неверную команду, почему твой UID =\n %d"%uid)


def run():
    global trusted
    trusted = []
    if os.path.exists("trusted.txt"):
        trusted = open("trusted.txt", "r").readlines()
    trusted_file = open("trusted.txt", "w")
    print(' >>> Run Telegram bot')
    bot.polling()
