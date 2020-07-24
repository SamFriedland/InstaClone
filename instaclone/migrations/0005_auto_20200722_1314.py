# Generated by Django 3.0.8 on 2020-07-22 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0004_auto_20200721_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaclone.InstaPost'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaclone.InstaPost'),
        ),
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together={('user_id', 'following_user_id')},
        ),
    ]
