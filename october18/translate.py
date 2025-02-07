
import tkinter as tk
import requests

class YandexTranslator:
    def __init__(self,token, catalog):
        self.token = token
        self.catalog = catalog

    def send_requests(self, text):
        url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'

        payload = {
            "sourceLanguageCode": "ru",
            "targetLanguageCode": "en",
            "format": "HTML",
            "texts": [
                f"{text}"
            ],
            "folderId": f"{self.catalog}",
            "speller": False
        }

        headers = {
            "Content_Type": "application/json",
            "Authorization": f"Api-Key {self.token}"
        }

        response = requests.post(url, headers=headers, json=payload)
        text = response.json()['translations'][0]['text']
        return text


class GraphicView():
    def __init__(self, bot):
        self._create_window()
        self.bot = bot
        self.root.mainloop()

    def _create_window(self):
        self.root = tk.Tk()
        self.root.title('тестовое окошко')

        self.input = tk.Text(self.root, height=10, width=20)
        self.input.grid(row=0, column=0, padx=10, pady=10)

        # окошко для вывода
        self.output = tk.Text(self.root, height=20, width=120)
        self.output.grid(row=0, column=1, padx=10, pady=10, rowspan=2)

        self.button = tk.Button(self.root, text='Отправить запрос', command=self.send_request)
        self.button.grid(row=2, column=0, padx=10, pady=10)


    def send_request(self):
        text = self.input.get('1.0', tk.END)

        response = self.bot.send_requests(text)
        print(response)

        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, response)



token = 'AQVNx-xYiG1GgnvTHG8-UF5Yw5p3PCuY92xGDuKz'
catalog = 'b1gtphdg2vndncqf33o7'
bot = YandexTranslator(token, catalog)

graphic_view = GraphicView(bot)

text = 'как тебя зовут?'

payload = {
            "sourceLanguageCode": "ru",
            "targetLanguageCode": "en",
            "format": "HTML",
            "texts": [
                f"{text}"
            ],
            "folderId": f"{catalog}",
            "speller": False
        }

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {token}"
}

url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
responce = requests.post(url, json=payload, headers=headers)
print(responce.json())