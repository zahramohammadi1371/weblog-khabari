# Generated by Django 4.0.6 on 2022-09-06 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0005_alter_post_created_time_alter_post_updeted_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated_time',
        ),
    ]