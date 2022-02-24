# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы получаем
# должность) с сайтов HH(обязательно). Приложение должно анализировать несколько страниц
# сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:

# 1. Наименование вакансии.
# 2. Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры
# преобразуем к цифрам).
# 3. Ссылку на саму вакансию.
# 4. Сайт, откуда собрана вакансия.

# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
# Структура должна быть одинаковая для вакансий с обоих сайтов.
# Общий результат можно вывести с помощью dataFrame через pandas. Сохраните в json либо csv.
import json
from pprint import pprint
from bs4 import BeautifulSoup
import requests

base_url = 'https://www.hh.ru/vacancies'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/98.0.4758.102 Safari/537.36'}
choice = input('Введите 1 для Учитель, 2 для Повар, 3 для Программист : ')

if choice == '1':
    choice = 'uchitel'
elif choice == '2':
    choice = 'povar'
elif choice == '3':
    choice = 'programmist'

job_title = "vacancy-serp__vacancy-title"
salary_tag = "vacancy-serp__vacancy-compensation"
job_link = "vacancy-serp__vacancy-title"
company_link = "vacancy-serp__vacancy-employer"

url = f'{base_url}/{choice}'
response = requests.get(url, headers=headers)
dom = BeautifulSoup(response.text, 'html.parser')

vacancies = dom.find_all('a', {'data-qa': 'vacancy-serp__vacancy-title'})
salaries = dom.find_all('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
companies = dom.find_all('a', {'data-qa': 'vacancy-serp__vacancy-employer'})

jobs = []
wages = []
links = []
company_names = []

for tag in vacancies:
    jobs.append(tag.text.strip())

for tag_2 in salaries:
    wages.append(tag_2.text.replace("\u202f", ' '))

for link in dom.find_all('a', {'data-qa': 'vacancy-serp__vacancy-title'}):
    links.append(link.get('href'))

for tag_3 in companies:
    company_names.append(tag_3.text.strip())

result = {}

for job, wage, link, company_name in zip(jobs, wages, links, company_names):
    result[f'{job}'] = f'{wage + link + company_name}'

with open('jobs_hh.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)




