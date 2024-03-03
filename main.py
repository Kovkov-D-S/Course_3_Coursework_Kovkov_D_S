# Импортируем модуль "os" для работы с файлами.
import os

# Импортируем функцию получения списка из json из файла functions.py
from utils.functions import load_operations

# Импортируем функцию получения 5 последних операций из файла functions.py
from utils.functions import last_operations

# Импортируем класс объекта из файла last_operations.py
from utils.last_operations import LastOperations


def main():
    """Запускает основной код программы."""
    for last_operation in last_operations():
        date_transfer = last_operation['date'].date()
        descrip_transfer = last_operation['description']
        recipient = last_operation['to']
        transfer_amount = last_operation['operationAmount']['amount']
        transfer_currency = last_operation['operationAmount']['currency']['name']
        if 'from' not in last_operation:
            sender = ''
        else:
            sender = last_operation['from']
        last_operation = LastOperations(tranf_date=date_transfer, descrip_transf=descrip_transfer, where_from=sender, where=recipient,
                              amount_transf=transfer_amount, currency_transf=transfer_currency)
        last_operation.format_date()
        last_operation.masking_card_numbers()
        last_operation.masking_bank_account()
        print(f'{last_operation.format_date()} {last_operation.descrip_transf}')
        print(f'{last_operation.masking_card_numbers()} -> {last_operation.masking_bank_account()}')
        print(f'{last_operation.amount_transf} {last_operation.currency_transf}\n')


# Запускаем основной код программы
main()