# Generated by Django 4.2.7 on 2023-12-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_kategoria_stan_alter_sprzet_rodzaj_alter_sprzet_stan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprzet',
            name='rodzaj',
            field=models.CharField(choices=[('snowboard', 'Snowboard'), ('narty', 'Narty'), ('buty_snowboardowe', 'Buty Snowboardowe'), ('buty_narciarskie', 'Buty Narciarskie'), ('kije', 'Kije Narciarskie')], max_length=17),
        ),
        migrations.AlterField(
            model_name='sprzet',
            name='stan',
            field=models.CharField(choices=[('BDB', 'Bardzo Dobry'), ('DB', 'Dobry'), ('OK', 'Jeszcze sprawny'), ('NOK', 'Nie sprawny')], max_length=3),
        ),
    ]
