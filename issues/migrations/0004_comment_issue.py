# Generated by Django 3.0.8 on 2020-08-04 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='issues.Issue', verbose_name='活动'),
        ),
    ]