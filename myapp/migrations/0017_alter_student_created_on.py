# Generated by Django 5.1.2 on 2024-10-23 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_student_created_on_student_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
