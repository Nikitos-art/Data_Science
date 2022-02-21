# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
import requests
import json

url = "https://api.vk.com/method/groups.get?v=5.131&access_token=c9d7a8c47d18152c4c890732a057f824249e33cda3c3f5f7e37ced1b11145e0d8314a13bb4e96fa6feb0c"


def api_reply(uri):
    response = requests.get(uri)
    j_data = response.json()
    j_data_to_str = json.dumps(j_data)
    ff = open('reply.json', 'w')
    ff.write(j_data_to_str)
    ff.close()


api_reply(url)