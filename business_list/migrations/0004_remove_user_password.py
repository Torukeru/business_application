# Generated by Django 5.0.6 on 2024-06-21 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_list', '0003_stall_stall_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
