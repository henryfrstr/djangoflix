# Generated by Django 3.2.4 on 2021-06-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_video_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='publish_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]