# Generated by Django 4.2.7 on 2024-01-15 15:53

from django.db import migrations, models
import item.models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0015_alter_utarg_data_alter_wypozyczenie_do_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utarg',
            name='kwota',
            field=models.FloatField(default=0, validators=[item.models.wiekszeOdZera]),
        ),
    ]