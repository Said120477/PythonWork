import requests
#saidMybot
token = '7992348444:AAF8Gc-OWI_bkiYLF8rHvBHjjznUSrJ6izw'
url = f'https://api.telegram.org/bot{token}/getMe'

url = f'https://api.telegram.org/bot{token}/getUpdates'

url_send = f'https://api.telegram.org/bot{token}/sendMessage'
user_bot = 1494760926
data = {'chat_id': user_bot, 'text': 'погода не очень'}
res = requests.get(url)

print(res.json())




