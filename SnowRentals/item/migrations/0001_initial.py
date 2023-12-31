# Generated by Django 4.2.7 on 2023-12-02 19:53

from django.db import migrations, models
import django.db.models.deletion
import item.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imie', models.CharField(max_length=40)),
                ('Nazwisko', models.CharField(max_length=40)),
                ('PESEL', models.CharField(max_length=11, unique=True)),
                ('Miasto', models.CharField(default='---', max_length=50)),
                ('Ulica_nrDomu', models.CharField(default='---', max_length=50)),
                ('Kod_pocztowy', models.CharField(max_length=6)),
                ('Nr_telefonu', models.CharField(max_length=9, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imie', models.CharField(max_length=40)),
                ('Nazwisko', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Sprzet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rodzaj', models.CharField(choices=[('SNB', 'Snowboard'), ('NRT', 'Narty'), ('BSNB', 'Buty Snowboardowe'), ('BNRT', 'Buty Narciarskie'), ('KIJE', 'Kije Narciarskie')], max_length=4)),
                ('Dlugosc', models.IntegerField(default=0, validators=[item.models.wiekszeOdZera])),
                ('Marka', models.CharField(max_length=40)),
                ('Stan', models.CharField(choices=[('BDB', 'Bardzo Dobry'), ('DB', 'Dobry'), ('OK', 'Jeszcze sprawny'), ('NOK', 'Nie sprawny')], max_length=3)),
                ('Cena', models.IntegerField(default=30, validators=[item.models.wiekszeOdZera])),
            ],
        ),
        migrations.CreateModel(
            name='Utarg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.DateTimeField(verbose_name='Utarg z dnia: ')),
                ('Kwota', models.FloatField(validators=[item.models.wiekszeOdZera])),
            ],
        ),
        migrations.CreateModel(
            name='Wypozyczenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Od', models.DateTimeField(verbose_name='Wypozyczone: ')),
                ('Do', models.DateTimeField(verbose_name='Zwrocone: ')),
                ('Zaplacone', models.BooleanField(default=False)),
                ('klient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.klient')),
                ('pracownik', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.pracownik')),
            ],
        ),
        migrations.CreateModel(
            name='Pakiet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sprzet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.sprzet')),
                ('wypozyczenie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.wypozyczenie')),
            ],
        ),
    ]
