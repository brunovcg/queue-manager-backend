# Generated by Django 3.2.9 on 2021-12-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='number',
            field=models.CharField(max_length=6),
        ),
    ]
