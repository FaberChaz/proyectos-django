# Generated by Django 3.2.6 on 2022-01-22 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]