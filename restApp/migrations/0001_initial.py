# Generated by Django 5.1.7 on 2025-03-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=20)),
            ],
        ),
    ]
