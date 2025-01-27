# Generated by Django 5.1.2 on 2024-10-27 17:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0003_department_hod_department_school_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='department',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
