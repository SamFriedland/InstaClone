# Generated by Django 3.0.8 on 2020-07-30 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instapost',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='emptyprofilepic.jpg', upload_to='images'),
        ),
    ]
