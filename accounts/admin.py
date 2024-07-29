from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'bio', 'birth_date', 'cpf_cnpj', 'description', 'avatar', 'phone_number', 'address', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'birth_date', 'cpf_cnpj', 'description', 'avatar', 'phone_number', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio', 'birth_date', 'cpf_cnpj', 'description', 'avatar', 'phone_number', 'address')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
