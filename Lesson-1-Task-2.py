# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
import requests
import json

url = ""


def api_reply(uri):
    response = requests.get(uri)
    j_data = response.json()
    j_data_to_str = json.dumps(j_data)
    ff = open('reply.json', 'w')
    ff.write(j_data_to_str)
    ff.close()


api_reply(url)
