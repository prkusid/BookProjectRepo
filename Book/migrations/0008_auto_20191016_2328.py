# Generated by Django 2.2.6 on 2019-10-16 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0007_auto_20191016_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='buser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
