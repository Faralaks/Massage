from datetime import timedelta
from os import path, getcwd
DEBUG = True
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