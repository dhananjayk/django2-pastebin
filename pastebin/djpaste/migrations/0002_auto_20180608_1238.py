# Generated by Django 2.0.6 on 2018-06-08 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djpaste', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasteobject',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
