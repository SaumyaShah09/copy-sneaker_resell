# Generated by Django 4.2.4 on 2024-04-11 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sneaker', '0012_ngo_password_alter_ngo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngo',
            name='password',
        ),
        migrations.AlterField(
            model_name='ngo',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
