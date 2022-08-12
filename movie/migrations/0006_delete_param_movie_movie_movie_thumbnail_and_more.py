# Generated by Django 4.1 on 2022-08-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_favourites_alter_movie_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Param',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie',
            field=models.FileField(null=True, upload_to='movies/movie/%y%m%d'),
        ),
        migrations.AddField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='movies/thumbnails/%y%m%d'),
        ),
        migrations.DeleteModel(
            name='Prefence',
        ),
    ]