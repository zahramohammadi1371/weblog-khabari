# Generated by Django 4.0.6 on 2022-09-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0004_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_time'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updeted_time',
            field=models.DateTimeField(auto_now=True, verbose_name='updeted_time'),
        ),
    ]
