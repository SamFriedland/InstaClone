# Generated by Django 3.0.8 on 2020-07-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0006_auto_20200726_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='/images/emptyprofilepic', upload_to='images/'),
        ),
    ]
