# Generated by Django 5.1.2 on 2024-10-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_student_class_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_teacher',
            field=models.CharField(max_length=50),
        ),
    ]
