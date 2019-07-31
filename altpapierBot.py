# -*- coding: utf-8 -*-

import telegram
import datetime
from datetime import date
from datetime import timedelta
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

# load environment variables from .env file
# it seems, the .env is not found in the current directory by default
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))


# initialize bot
token = os.getenv('TELEGRAM_BOT_TOKEN')
chatId = os.getenv('TELEGRAM_CHAT_ID')
print("Token: %s, chatId: %s" % (token, chatId))

bot = telegram.Bot(token=token)

# get date from OpenERZ API
today = date.today()
tomorrow = date.today() + timedelta(days=1)
zip = os.getenv('ZIP_CODE')
tour = os.getenv('TOUR', '')
types = {
    'paper': 'Altpapier',
    'cardboard': 'Karton',
}
for type, descr in types.items():
    url = (
        "http://openerz.metaodi.ch/api/calendar.json?types=%s&zip=%s&tour=%s&start=%s&sort=date&offset=0&limit=1"
        % (type, zip, tour, today.isoformat())
    )
    print("URL: %s" % url)
    r = requests.get(url)
    nextDateStr = r.json()['result'][0]['date']
    nextDate = datetime.datetime.strptime(nextDateStr, '%Y-%m-%d').date()

    # send message if nextDate is today or tomorrow
    msg = ''
    if nextDate == tomorrow:
        msg = "Morn isch imfall %s!" % descr
    if nextDate == today:
        msg = "Hüt isch imfall %s!" % descr

    print('Message: %s' % msg)
    if msg:
        bot.sendMessage(chatId, msg)
