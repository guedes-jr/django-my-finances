from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=18, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    def get_data_birth_date(self):
        return self.birth_date.strftime('%Y-%m-%d')

    def __str__(self):
        return self.username
