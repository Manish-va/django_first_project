# Generated by Django 5.1.2 on 2024-10-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0002_school_created_on_school_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]