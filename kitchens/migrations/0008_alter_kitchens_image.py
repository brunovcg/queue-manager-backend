# Generated by Django 3.2.9 on 2021-12-11 02:53

from django.db import migrations, models
import kitchens.models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchens', '0007_alter_kitchens_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchens',
            name='image',
            field=models.FileField(blank=True, default='default.jpg', upload_to=kitchens.models.upload_to),
        ),
    ]