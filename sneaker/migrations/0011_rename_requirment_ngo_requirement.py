# Generated by Django 4.2.4 on 2024-03-23 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneaker', '0010_alter_ngo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ngo',
            old_name='requirment',
            new_name='requirement',
        ),
    ]