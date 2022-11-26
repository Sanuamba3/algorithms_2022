"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib

cashe = {}

def get_hash(url):
    salt = 'peper'
    res = hashlib.sha256((url + salt).encode()).hexdigest()
    return res

def add_url(url):
    if cashe.get(url):
        print(f'URL - {url} уже сохранен в кэше')
    else:
        urls_hash = get_hash(url)
        cashe[url] = urls_hash
        print(cashe)


add_url('http://problems.net')
add_url('https://hello.world/')
add_url('http://problems.net')