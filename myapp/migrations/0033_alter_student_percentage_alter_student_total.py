# Generated by Django 5.1.2 on 2024-11-04 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_remove_student_chemistry_remove_student_maths_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='percentage',
            field=models.FloatField(default=0.0, editable=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='total',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
