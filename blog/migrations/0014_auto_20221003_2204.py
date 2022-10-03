# Generated by Django 3.2.7 on 2022-10-03 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_game_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
        migrations.AddField(
            model_name='game',
            name='pub',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
    ]