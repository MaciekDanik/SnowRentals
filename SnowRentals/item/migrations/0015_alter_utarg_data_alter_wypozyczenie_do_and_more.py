# Generated by Django 4.2.7 on 2024-01-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0014_sprzet_wypozyczone_alter_wypozyczenie_klient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utarg',
            name='data',
            field=models.DateField(verbose_name='Utarg z dnia: '),
        ),
        migrations.AlterField(
            model_name='wypozyczenie',
            name='do',
            field=models.DateField(verbose_name='Zwrocone: '),
        ),
        migrations.AlterField(
            model_name='wypozyczenie',
            name='od',
            field=models.DateField(verbose_name='Wypozyczone: '),
        ),
    ]
