# Generated by Django 4.1.1 on 2022-09-30 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instauser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instauser',
            name='is_dating',
            field=models.BooleanField(null=True),
        ),
    ]