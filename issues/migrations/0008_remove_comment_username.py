# Generated by Django 3.0.8 on 2020-08-04 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_comment_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
    ]
