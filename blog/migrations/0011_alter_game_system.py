# Generated by Django 3.2.7 on 2022-09-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20220926_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='system',
            field=models.TextField(verbose_name='Системные требования'),
        ),
    ]
