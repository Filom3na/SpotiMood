# Generated by Django 5.0.6 on 2024-06-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_music', '0007_remove_song_mood_playlist_song_mood_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='mood_playlist',
            field=models.ManyToManyField(blank=True, related_name='songs', to='mood_music.moodplaylist'),
        ),
    ]