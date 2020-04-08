#!/usr/bin/python

import requests
import sys
import urllib

TELEGRAM_APITOKEN='<your_api_token_here>'
TELEGRAM_CHATID='<your_chat_id_here>'

message = sys.stdin.read()

if len(message) > 4096:
    message = message[:4092] + ' ...'

query = urllib.quote(message)

result = requests.get('https://api.telegram.org/bot' + TELEGRAM_APITOKEN + '/sendMessage?chat_id=' + TELEGRAM_CHATID + '&text=' + query)

if result.status_code != 200:
  sys.exit(1)

