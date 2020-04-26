import os

DEBUG = True

BOT_TOKEN = os.getenv('EXPENSE_BOT_TOKEN')
BOT_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'
BOT_CHAT_ID = os.getenv('BOT_CHAT_ID')

DB_USER = os.getenv('TG_EXPENSE_BOT_DB_USER')
DB_PASS = os.getenv('TG_EXPENSE_BOT_DB_PASS')
DB_NAME = os.getenv('TG_EXPENSE_BOT_DB_NAME')
DB_HOST = os.getenv('TG_EXPENSE_BOT_DB_HOST')
DB_PORT = os.getenv('TG_EXPENSE_BOT_DB_PORT')
