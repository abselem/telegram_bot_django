# Generated by Django 3.2 on 2023-09-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=255, unique=True)),
                ('token', models.CharField(max_length=255)),
            ],
        ),
    ]
