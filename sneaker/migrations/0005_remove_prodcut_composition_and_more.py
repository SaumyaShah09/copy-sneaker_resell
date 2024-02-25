# Generated by Django 4.2.4 on 2024-02-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaker', '0004_alter_prodcut_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prodcut',
            name='composition',
        ),
        migrations.RemoveField(
            model_name='prodcut',
            name='discounted_price',
        ),
        migrations.RemoveField(
            model_name='prodcut',
            name='selling_price',
        ),
        migrations.AddField(
            model_name='prodcut',
            name='email',
            field=models.EmailField(default='xyz@gmail.com', max_length=250),
        ),
    ]