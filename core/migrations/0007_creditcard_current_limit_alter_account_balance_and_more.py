# Generated by Django 5.0.7 on 2024-08-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_creditcard_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='current_limit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Limite'),
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Balanço'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='limit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Limite'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='current_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Valor atual'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='targeted_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Valor Almejado'),
        ),
    ]
