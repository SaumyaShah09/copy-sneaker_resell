# Generated by Django 4.2.4 on 2024-02-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaker', '0006_ngo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='requirment',
            field=models.CharField(default='fashion', max_length=100),
        ),
    ]
