# Generated by Django 5.1.2 on 2024-10-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_student_percentage_student_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]