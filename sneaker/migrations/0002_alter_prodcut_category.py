# Generated by Django 4.2.4 on 2023-09-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodcut',
            name='category',
            field=models.CharField(choices=[('CR', 'Curd'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('KL', 'Kulfi'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IC', 'Ice creams')], max_length=2),
        ),
    ]
