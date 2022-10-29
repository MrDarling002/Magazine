# Generated by Django 3.2.7 on 2022-10-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_rename_main_image_game_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Категория игры')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Game_dev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
            ],
        ),
    ]
