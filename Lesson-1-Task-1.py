# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.


import json
import requests


### User examples Nikitos-art or Nikolos123

def requestUserRepos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    j_data = response.json()
    final_repo_list = {}
    for i in range(len(j_data)):
        final_repo_list.update({j_data[i]["id"]:j_data[i]["name"]})
    filtered_repo_list_to_json = json.dumps(final_repo_list, indent=4)
    ff = open('repo_list.json', 'w')
    ff.write(filtered_repo_list_to_json)
    ff.close()


user_input = input('Enter username: ')
requestUserRepos(user_input)





# def requestUserRepos(username):
#     url = f"https://api.github.com/users/{username}/repos"
#     response = requests.get(url)
#     j_data = response.json()
#     final_repo_list = []
#     for i in range(len(j_data)):
#         final_repo_list.append(j_data[i]["full_name"])
#     filtered_repo_list_to_json = json.dumps(final_repo_list, indent=4)
#     ff = open('repo_list.json', 'w')
#     ff.write(filtered_repo_list_to_json)
#     ff.close()
#
#
# user_input = input('Enter username: ')
# requestUserRepos(user_input)



















# def requestUserRepos(username):
#     url = f"https://api.github.com/users/{username}/repos"
#     response = requests.get(url)
#     j_data = response.json()
#     with open('data.json', 'w') as json_file:
#         json_file.write(j_data)
#         # data = json.load(json_file)
#         # data.write(j_data)
#
# requestUserRepos("Nikitos-art")
