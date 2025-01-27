# Generated by Django 5.1.2 on 2024-10-30 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0007_remove_department_school_id'),
        ('School', '0003_school_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='departments',
            field=models.ManyToManyField(related_name='schools', to='Department.department'),
        ),
    ]
