# Generated by Django 5.1.2 on 2024-11-03 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete_status'], 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]