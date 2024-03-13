import os
import json

import pytest

from utils.functions import last_operations
from utils.last_operations import LastOperations


@pytest.fixture
def test_operations():
    return [
        {"date": "2024-03-05T12:00:00.000", "state": "EXECUTED"},
        {"date": "2024-03-06T12:00:00.000", "state": "FAILED"},
        {"date": "2024-03-07T12:00:00.000", "state": "EXECUTED"},
        {"date": "2024-03-08T12:00:00.000", "state": "EXECUTED"},
        {"date": "2024-03-09T12:00:00.000", "state": "EXECUTED"}
    ]


@pytest.fixture
def operations_file(tmpdir, test_operations):
    file_path = os.path.join(tmpdir, 'operations.json')
    with open(file_path, 'w') as f:
        json.dump(test_operations, f)
    return file_path


def test_load_operations(test_operations, operations_file):
    with open(operations_file, 'r', encoding="utf-8") as operations:
        loaded_operations = json.loads(operations.read())
        assert loaded_operations == test_operations


def test_last_operations():
    """
    Этот тест частично даже большая часть из main твоего взят.
    """
    test_list_last_operations = []
    for operation in last_operations():
        date_transfer = operation['date'].date()
        descript_transfer = operation['description']  # Тут опечатка у тебя была в переменной. Сделал по PEP8
        recipient = operation['to']
        transfer_amount = operation['operationAmount']['amount']
        transfer_currency = operation['operationAmount']['currency']['name']
        if 'from' not in operation:
            sender = ''
        else:
            sender = operation['from']
        operation = LastOperations(tranf_date=date_transfer, descrip_transf=descript_transfer, where_from=sender,
                                   where=recipient,
                                   amount_transf=transfer_amount, currency_transf=transfer_currency)
        operation.format_date()
        test_list_last_operations.append({'date': operation.format_date(), 'state': 'EXECUTED'})

    expected_result = [
        {"date": '08.12.2019', "state": "EXECUTED"},
        {"date": '07.12.2019', "state": "EXECUTED"},
        {"date": '19.11.2019', "state": "EXECUTED"},
        {"date": '13.11.2019', "state": "EXECUTED"},
        {"date": '05.11.2019', "state": "EXECUTED"}
    ]
    # Здесь проверка тестом.
    assert test_list_last_operations == expected_result
