class LastOperations:

    def __init__(self, tranf_date, where_from=None, descrip_transf=None, where=None,
                          amount_transf=None, currency_transf=None):
        """Инициирует свойства класса.
        """
        self.tranf_date = tranf_date
        self.descrip_transf = descrip_transf
        self.where_from = where_from
        self.where = where
        self.amount_transf = amount_transf
        self.currency_transf = currency_transf

    def format_date(self):
        """Возвращает дату перевода в формате "День.Месяц.Год".
        """
        return self.tranf_date.strftime('%d.%m.%Y')

    def masking_card_numbers(self):
        """Возвращает информацию о том, откуда переведены денежные средства с замаскированными данными счета или карты.
        """
        if self.where_from != None or self.where_from != '' :
            type_card = ''.join(letter for letter in self.where_from if not letter.isdigit())
            card_number = ''.join(letters if letters.isdigit() else ' ' for letters in self.where_from).split()
            if card_number != []:
                masking_number = card_number[0][0:4] + ' ' + card_number[0][5:7] + '** ****' + ' ' + card_number[0][-4:]
            else:
                masking_number = ''
        return f'{type_card} {masking_number}'


    def masking_bank_account(self):
        """Возвращает информацию о том, куда переведены денежные средства с замаскированными данными счета или карты.
        """
        type_bank_account = ''.join(letter for letter in self.where if not letter.isdigit())
        bank_number = ''.join(letters if letters.isdigit() else ' ' for letters in self.where).split()
        masking_bank_number = '**'+ bank_number[0][-4:]
        return f'{type_bank_account} {masking_bank_number}'

    def __repr__(self):
        """Выводит читаемую информацию по описываемому классу.
        """
        return f"tranf_date - {self.tranf_date}, descrip_transf - {self.descrip_transf}, where_from - {self.where_from}, " \
               f"where - {self.where}, amount_transf - {self.amount_transf}, currency_transf - {self.currency_transf} "

