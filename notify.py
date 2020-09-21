#!/usr/bin/python3

import requests
import sys
import urllib

TELEGRAM_APITOKEN='<your_api_token_here>'
TELEGRAM_CHATID='<your_chat_id_here>'
MAX_LENGTH=4096

message = sys.stdin.read()

def send(message):
  query = urllib.parse.quote(message)
  result = requests.get('https://api.telegram.org/bot' + TELEGRAM_APITOKEN + '/sendMessage?chat_id=' + TELEGRAM_CHATID + '&text=' + query)
  if result.status_code != 200:
    sys.exit(1)

part = message

while len(part) > MAX_LENGTH:
  send(part[:MAX_LENGTH])
  part = part[MAX_LENGTH:]

send(part)

