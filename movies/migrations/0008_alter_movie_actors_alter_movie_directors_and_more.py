# Generated by Django 4.1.6 on 2023-02-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("movies", "0007_alter_cast_full_name")]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(
                blank=True, related_name="movie_actors", to="movies.cast"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="directors",
            field=models.ManyToManyField(
                blank=True, related_name="movie_directors", to="movies.cast"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="writers",
            field=models.ManyToManyField(
                blank=True, related_name="movie_writers", to="movies.cast"
            ),
        ),
    ]
