# Generated by Django 4.1 on 2022-08-09 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_newuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
