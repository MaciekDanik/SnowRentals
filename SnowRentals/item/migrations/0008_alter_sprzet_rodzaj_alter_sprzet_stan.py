# Generated by Django 4.2.7 on 2023-12-06 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_alter_kategoria_options_alter_stan_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprzet',
            name='rodzaj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.kategoria'),
        ),
        migrations.AlterField(
            model_name='sprzet',
            name='stan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.stan'),
        ),
    ]
