# Generated by Django 4.2.1 on 2023-05-16 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_details',
            name='img',
            field=models.ImageField(default='abcd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]