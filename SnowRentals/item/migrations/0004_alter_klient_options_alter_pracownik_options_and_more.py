# Generated by Django 4.2.7 on 2023-12-02 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_sprzet_rodzaj'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='klient',
            options={'ordering': ('imie',), 'verbose_name_plural': 'Klienci'},
        ),
        migrations.AlterModelOptions(
            name='pracownik',
            options={'ordering': ('imie',), 'verbose_name_plural': 'Pracownicy'},
        ),
        migrations.AlterModelOptions(
            name='sprzet',
            options={'ordering': ('rodzaj',), 'verbose_name_plural': 'Lista sprzętu'},
        ),
        migrations.AlterModelOptions(
            name='utarg',
            options={'ordering': ('data',), 'verbose_name_plural': 'Kategorie'},
        ),
    ]
