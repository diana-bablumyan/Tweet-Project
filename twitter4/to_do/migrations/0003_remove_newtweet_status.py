# Generated by Django 3.2.4 on 2021-06-30 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0002_auto_20210627_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newtweet',
            name='status',
        ),
    ]