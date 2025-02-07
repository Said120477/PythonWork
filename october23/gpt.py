import requests

class YandexGpt:
    def __init__(self, token, catalog):
        self.token = token
        self.catalog = catalog


    def send_requests(self, questions):
        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

        prompt = {
            "modelUri": f'gpt://{self.catalog}/yandexgpt-lite',
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": 200
            },
            "messages": [

            {
            "role": "user",
            "text": f"{questions}"
            }
            ]
            }

        headers = {
            "Content_Type": "application/json",
            "Authorization": f"Api-Key {self.token}"
        }

        response = requests.post(url, headers=headers, json=prompt)
        text = response.json()['result']['alternatives'][0]['message']['text']
        return text

# token = 'AQVNwS23Dd2gP_MApsCmoaP0G4qg7IH2Uvwb3cdQ'
# catalog = 'b1gf0ql594j8i8rv3ner'
#
# bot = YandexGpt(token, catalog)
# res = bot.send_requests('что такое любовь?')
# print(res)
