# Generated by Django 5.1.2 on 2024-10-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_student_percentage_remove_student_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_teacher',
            field=models.CharField(default='Mr. Manish', max_length=50),
        ),
    ]