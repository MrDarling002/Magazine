# Generated by Django 3.2.7 on 2022-10-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20221029_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game_dev',
            name='youtube',
        ),
        migrations.AddField(
            model_name='game_category',
            name='youtube',
            field=models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Ссылка на видео'),
        ),
    ]