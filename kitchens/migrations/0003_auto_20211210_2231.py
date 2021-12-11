# Generated by Django 3.2.9 on 2021-12-11 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kitchens', '0002_auto_20211205_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchens',
            name='branch',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='kitchens', to='branches.branches'),
        ),
        migrations.AlterField(
            model_name='kitchens',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='kitchens', to=settings.AUTH_USER_MODEL),
        ),
    ]
