# Generated by Django 5.1.2 on 2024-11-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='password',
            field=models.CharField(default='default_password', max_length=16),
        ),
    ]