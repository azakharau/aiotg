import os

BOT_TOKEN = os.getenv('EXPENSE_BOT_TOKEN')

API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'
