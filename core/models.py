from django.core.exceptions import ValidationError
from accounts.models import CustomUser
from django.utils import timezone
from django.db import models
import re
from . import constants

class Account(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=50, verbose_name="Nome para a conta")
    account_type = models.CharField(max_length=20, choices=constants.ACCOUNT_TYPES, default='OTHER', verbose_name="Tipo de Conta")
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Balanço")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_account_type_display(self):
        return dict(constants.ACCOUNT_TYPES).get(self.account_type, 'Desconhecido')

    def get_format_balance(self):
        return str(self.balance)

    def __str__(self):
        return f"{self.account_name} - {self.get_account_type_display()}"

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="Conta")
    category = models.CharField(max_length=20, choices=constants.CATEGORY_CHOICES, default='OTHER', verbose_name="Categoria")
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Valor da transação")
    transaction_date = models.DateField(default=timezone.now, verbose_name="Data em que foi realizado a transação")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    transaction_type = models.CharField(max_length=10, choices=constants.TRANSACTION_TYPES, verbose_name="Tipo de Transação")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_transaction_type_display(self):
        return dict(constants.TRANSACTION_TYPES).get(self.transaction_type, 'Desconhecido')

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.value}"

class CreditCard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=20, choices=constants.CARD_TYPES, default='OTHER', verbose_name="Tipo de Cartão")
    surname = models.TextField(blank=True, null=True, verbose_name="Apelido")
    card_number = models.CharField(max_length=19, verbose_name="Número do Cartão")
    cardholder_name = models.CharField(max_length=100, verbose_name="Nome do Titular")
    expiration_date = models.DateField(verbose_name="Data de Validade")
    security_code = models.CharField(max_length=4, verbose_name="Código de Segurança (CVV)")
    limit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Limite")

    def __str__(self):
        return f"{self.cardholder_name} - {self.card_type}"

    class Meta:
        verbose_name = "Cartão de Crédito"
        verbose_name_plural = "Cartões de Crédito"

    def mask_card_number(self):
        return f"**** **** **** {self.card_number[-4:]}"

    def clean(self):
        self.card_type = self.identify_card_type(self.card_number)
        if self.card_type == 'UNKNOWN':
            raise ValidationError('Número do cartão inválido ou bandeira não reconhecida.')

    @staticmethod
    def identify_card_type(card_number):
        card_number = re.sub(r'[\s-]', '', card_number)  # Remove espaços e traços
        if re.match(r'^4[0-9]{12}(?:[0-9]{3})?$', card_number):
            return 'VISA'
        elif re.match(r'^5[1-5][0-9]{14}$', card_number):
            return 'MASTERCARD'
        elif re.match(r'^3[47][0-9]{13}$', card_number):
            return 'AMEX'
        elif re.match(r'^6(?:011|5[0-9]{2})[0-9]{12}$', card_number):
            return 'DISCOVER'
        else:
            return 'UNKNOWN'

class Goal(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=constants.CATEGORY_CHOICES, default='OTHER', verbose_name="Categoria")
    description = models.TextField(verbose_name="Descrição")
    current_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor atual")
    targeted_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Almejado")
    start_date = models.DateField(verbose_name="Data de início")
    end_date = models.DateField(verbose_name="Data final para meta")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_format_current_value(self):
        return str(self.current_value)

    def get_format_targeted_value(self):
        return str(self.targeted_value)
    
    def get_category_type_display(self):
        return dict(constants.CATEGORY_CHOICES).get(self.category, 'Desconhecido')
    
    def get_data_start_date(self):
        return self.start_date.strftime('%Y-%m-%d')
    
    def get_data_end_date(self):
        return self.end_date.strftime('%Y-%m-%d')

    def __str__(self):
        return f"{self.description[:25]} - {self.current_value} -> ({self.targeted_value} to {self.start_date} -> {self.end_date})"
