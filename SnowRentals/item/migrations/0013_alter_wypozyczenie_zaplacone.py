# Generated by Django 4.2.7 on 2023-12-25 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0012_alter_bool_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wypozyczenie',
            name='zaplacone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.bool'),
        ),
    ]
