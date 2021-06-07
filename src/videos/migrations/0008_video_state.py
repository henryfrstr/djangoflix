# Generated by Django 3.2.4 on 2021-06-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20210607_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Publish'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]
