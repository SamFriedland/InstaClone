# Generated by Django 3.0.8 on 2020-08-01 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='InstaPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='posts')),
                ('post_title', models.CharField(max_length=200, null=True)),
                ('caption', models.CharField(max_length=500, null=True)),
                ('pub_date', models.DateTimeField(null=True, verbose_name='Date Published')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100, null=True)),
                ('profile_picture', models.ImageField(default='emptyprofilepic.jpg', upload_to='profile_pic')),
                ('bio', models.CharField(default='', max_length=500, null=True)),
                ('d_o_b', models.DateTimeField(null=True, verbose_name='Date of birth')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaclone.InstaPost')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='instaclone.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='instapost',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='instaclone.Profile'),
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaclone.Comment')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='instaclone.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaclone.InstaPost'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instaclone.Profile'),
        ),
        migrations.CreateModel(
            name='UserFollowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='instaclone.Profile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='instaclone.Profile')),
            ],
            options={
                'unique_together': {('user_id', 'following_user_id')},
            },
        ),
    ]
