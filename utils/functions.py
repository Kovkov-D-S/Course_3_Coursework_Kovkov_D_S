# Импортируем формат файлов "json".
import json


# Импортируем модуль "os" для работы с файлами.
import os


# Импортируем модуль "datetime" для перевода даты в стороком виде с формат даты.
from datetime import datetime


# Импортируем класс объекта из файла created_words.py
from utils.last_operations import LastOperations


# Строим пути к файлам с учетом особенностей ОС.
file_operations = os.path.join('.\src', 'operations.json')


def load_operations():
    """Загружает список транзакций из файла "operations.json"."""
    with open(file_operations, 'r', encoding="utf-8") as operations:
        list_operations = json.loads(operations.read())
        return list_operations


def last_operations():
    """Получам список из 5 самых свежих транзакций клиента и возвращаем как объект класса."""
    operations_list = load_operations()
    list_last_operations = []
    for operation in operations_list:
        if operation == {}:
            continue
        date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')
        if operation['state'] == 'EXECUTED':
            list_last_operations.append(operation)
        operation['date'] = date
        list_last_operations = sorted(list_last_operations, key=lambda x: x['date'], reverse=True)
    five_last_operations = list_last_operations[:5]
    return five_last_operations
