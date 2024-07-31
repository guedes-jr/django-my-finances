from django.contrib import admin

from django.contrib import admin
from .models import CreditCard

@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('cardholder_name', 'card_type', 'mask_card_number', 'expiration_date')
    search_fields = ('cardholder_name', 'card_number')
    readonly_fields = ('mask_card_number',)
