# Generated by Django 5.0.6 on 2024-06-03 01:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_music', '0002_mood_user_alter_moodentry_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moodentry',
            name='owner',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='owned_mood_entries', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moodplaylist',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owned_mood_playlists', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mood',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moods', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='moodentry',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mood_entries', to=settings.AUTH_USER_MODEL),
        ),
    ]
