# Generated by Django 5.1.2 on 2024-10-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_student_class_teacher_teacher_performance'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
