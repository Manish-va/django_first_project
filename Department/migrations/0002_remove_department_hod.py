# Generated by Django 5.1.2 on 2024-10-24 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='hod',
        ),
    ]
