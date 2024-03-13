import os

import unittest

import datetime

from utils.last_operations import LastOperations


class TestLastOperations(unittest.TestCase):

    def test_format_date(self):
        result1 = datetime.datetime(2019, 12, 8, 22, 46, 21, 935582).strftime('%d.%m.%Y')
        self.assertEqual(result1, '08.12.2019')
        result2 = datetime.datetime(2019, 12, 7, 6, 17, 14, 634890).strftime('%d.%m.%Y')
        self.assertEqual(result2, '07.12.2019')


    def test_masking_card_numbers(self):
        self.where_from = 'Visa Classic 2842878893689012'
        type_card = ''.join(letter for letter in self.where_from if not letter.isdigit())
        card_number = ''.join(letters if letters.isdigit() else ' ' for letters in self.where_from).split()
        masking_number = card_number[0][0:4] + ' ' + card_number[0][5:7] + '** ****' + ' ' + card_number[0][-4:]
        result = type_card + ' ' + masking_number
        self.assertEqual(result, 'Visa Classic  2842 78** **** 9012')
        self.where_from = []
        self.assertEqual(self.where_from , [])


    def test_masking_bank_account(self):
        self.where = 'Счет 35158586384610753655'
        type_bank_account = ''.join(letter for letter in self.where if not letter.isdigit())
        bank_number = ''.join(letters if letters.isdigit() else ' ' for letters in self.where).split()
        masking_bank_number = '**' + bank_number[0][-4:]
        result = type_bank_account + ' ' + masking_bank_number
        self.assertEqual(result, 'Счет  **3655')


    def test__init__(self):
        self.assertRaises(TypeError, LastOperations)

    def test__repr__(self):
        date_transfer = datetime.datetime(2019, 12, 8, 22, 46, 21, 935582)
        sender = None
        descrip_transfer = 'Открытие вклада'
        recipient = 'Счет 90424923579946435907'
        transfer_amount = '41096.24'
        transfer_currency = 'USD'
        exaple = LastOperations(tranf_date=date_transfer, descrip_transf=descrip_transfer, where_from=sender,
                                where=recipient, amount_transf=transfer_amount, currency_transf=transfer_currency)
        result = exaple.__repr__()
        self.assertEqual(result, f"tranf_date - 2019-12-08 22:46:21.935582, descrip_transf - Открытие вклада,"
                                 f" where_from - None, " 
               f"where - Счет 90424923579946435907, amount_transf - 41096.24, currency_transf - USD ")



