# Generated by Django 4.1.6 on 2023-02-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("movies", "0010_alter_genre_options_remove_genre_level_and_more")]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="title",
            field=models.CharField(
                db_index=True,
                help_text="Movie title",
                max_length=150,
                verbose_name="Movie title",
            ),
        )
    ]
