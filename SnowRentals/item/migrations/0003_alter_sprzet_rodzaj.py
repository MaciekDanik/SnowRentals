# Generated by Django 4.2.7 on 2023-12-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_klient_options_alter_pakiet_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprzet',
            name='rodzaj',
            field=models.CharField(choices=[('snowboard', 'Snowboard'), ('narty', 'Narty'), ('buty_snowboardowe', 'Buty Snowboardowe'), ('buty_narciarskie', 'Buty Narciarskie'), ('kije', 'Kije Narciarskie')], max_length=17),
        ),
    ]
