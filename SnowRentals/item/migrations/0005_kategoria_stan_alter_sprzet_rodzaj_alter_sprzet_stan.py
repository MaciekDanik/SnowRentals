# Generated by Django 4.2.7 on 2023-12-06 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_alter_klient_options_alter_pracownik_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategoria', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='Stan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stan', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Stany',
            },
        ),
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
