# Generated by Django 5.0 on 2024-01-03 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Tweet',
        ),
    ]
