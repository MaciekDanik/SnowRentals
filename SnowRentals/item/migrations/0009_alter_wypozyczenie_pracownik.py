# Generated by Django 4.2.7 on 2023-12-10 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0008_alter_sprzet_rodzaj_alter_sprzet_stan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wypozyczenie',
            name='pracownik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
    ]
