# Generated by Django 3.2.4 on 2021-07-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('date_send', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
