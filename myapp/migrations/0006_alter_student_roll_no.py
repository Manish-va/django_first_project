# Generated by Django 5.1.2 on 2024-10-18 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_student_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.AutoField(max_length=10, primary_key=True, serialize=False),
        ),
    ]