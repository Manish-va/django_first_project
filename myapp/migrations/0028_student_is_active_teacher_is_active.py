# Generated by Django 5.1.2 on 2024-10-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_student_department_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]