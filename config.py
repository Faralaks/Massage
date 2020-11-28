from datetime import timedelta
from os import path, getcwd
DEBUG = False
PORT = 5000
HOST = "0.0.0.0"
DB_PATH = path.join(getcwd(), 'db', 'db.sqlite')
SECRET_KEY = 'secret'
TEMPLATES_AUTO_RELOAD = True
LOGIN = "login"
PAS = 'pas'
COOKIE_SECURE = 'Secure'
COOKIE_DURATION = timedelta(days=5)
TELEGRAM_TOKEN = ""
TRUSTED = {}
AUTO_DB_SEND_PERIOD = 86400 #24 hour
AUTO_CUR_XL_SEND_PERIOD = 604800 # 7 days
AUTO_PREV_XL_SEND_PERIOD = 1209600 # 14 days
AUTO_SEND_RECIPIENT = {}