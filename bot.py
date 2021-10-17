import time
import zipfile
from io import BytesIO

from app import make_xlsx, o_make_xlsx
from config import DB_PATH, AUTO_DB_SEND_PERIOD, AUTO_SEND_RECIPIENT, AUTO_ZIP_SEND_PERIOD


def send_db(uid, bot):
    base = open(DB_PATH, "rb")
    bot.send_document(uid, caption="На! Свою Базу!", data=base)
    base.close()


def send_files(uid, bot):
    streams = {
        "Массажный отчет за этот месяц":make_xlsx(BytesIO(), "cur"),
        "Массажный отчет за предыдущий месяц":make_xlsx(BytesIO(), "prev"),
        "Авто-отчет за этот месяц":o_make_xlsx(BytesIO(), "cur"),
        "Авто-отчет за предыдущий месяц":o_make_xlsx(BytesIO(), "prev")}

    zip_file = BytesIO()
    with zipfile.ZipFile(zip_file, mode="w") as z:
        for name, value in streams.items():
            z.writestr(name+".xlsx", value)

    zip_file.name = "all_data.zip"
    zip_file.seek(0)
    bot.send_document(uid, caption="На! Свой зип!", data=zip_file, disable_notification=True)



def db_auto_sender(bot):
    print(' >>> Run Telegram bot db_auto_sender')
    while True:
        for uid in AUTO_SEND_RECIPIENT:
            time.sleep(2)
            print(' >>> db send to  ' + str(uid))
            try: send_db(uid, bot)
            except:
                print("А я все равно отправлю!")
                time.sleep(3)
                send_db(uid, bot)
        time.sleep(AUTO_DB_SEND_PERIOD)

def zip_auto_sender(bot):
    print(' >>> Run Telegram bot zip_auto_sender')
    while True:
        for uid in AUTO_SEND_RECIPIENT:
            print(' >>> ZIP send to  ' + str(uid))
            send_files(uid, bot)
        time.sleep(AUTO_ZIP_SEND_PERIOD)


def run(bot):
    print(' >>> Run Telegram bot listener')
    while True:
        try: bot.polling(interval=5)
        except: print("Не упал!")
