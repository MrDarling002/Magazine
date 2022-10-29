# Generated by Django 3.2.7 on 2022-10-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_game_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game_category',
            name='youtube',
        ),
        migrations.RemoveField(
            model_name='game_dev',
            name='dev_text',
        ),
        migrations.RemoveField(
            model_name='game_dev',
            name='dev_title',
        ),
        migrations.AddField(
            model_name='game_text',
            name='youtube',
            field=models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Ссылка на видео'),
        ),
    ]
