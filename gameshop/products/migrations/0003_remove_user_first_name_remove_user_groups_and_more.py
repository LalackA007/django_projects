# Generated by Django 5.1.2 on 2024-10-25 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_user_first_name_remove_user_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]