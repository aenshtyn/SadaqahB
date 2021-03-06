# Generated by Django 3.1.3 on 2020-11-27 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeals', '0004_auto_20201127_0902'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tags',
            new_name='Tag',
        ),
        migrations.RemoveField(
            model_name='appeal',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='tags',
        ),
        migrations.AddField(
            model_name='appeal',
            name='tag',
            field=models.ManyToManyField(to='appeals.Tag'),
        ),
        migrations.AddField(
            model_name='donation',
            name='tag',
            field=models.ManyToManyField(to='appeals.Tag'),
        ),
    ]
