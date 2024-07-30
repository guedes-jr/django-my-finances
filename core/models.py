from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('FOOD', 'Alimentação'),
        ('TRANSPORT', 'Transporte'),
        ('HOUSING', 'Moradia'),
        ('HEALTH', 'Saúde'),
        ('EDUCATION', 'Educação'),
        ('ENTERTAINMENT', 'Lazer e Entretenimento'),
        ('SHOPPING', 'Compras'),
        ('PERSONAL', 'Despesas Pessoais'),
        ('FINANCE', 'Finanças'),
        ('OTHER', 'Outros'),
        ('SALARY', 'Salário'),
        ('FREELANCE', 'Freelance'),
        ('RENTAL', 'Aluguéis'),
        ('INVESTMENTS', 'Investimentos'),
        ('GIFTS', 'Presentes'),
        ('SALES', 'Venda de Itens'),
        ('REIMBURSEMENTS', 'Reembolsos'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('CHECKING', 'Conta Corrente'),
        ('SAVINGS', 'Poupança'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=50)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_name} - {self.get_account_type_display()}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('DEBIT', 'Débito'),
        ('CREDIT', 'Crédito'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.amount}"

class Budget(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount} ({self.start_date} to {self.end_date})"
