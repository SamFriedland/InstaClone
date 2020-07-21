from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64)
    profile_picture = models.ImageField(upload_to="images", default='/emptyprofilepic')

    def __str__(self):
        return self.username
6

class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    following_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

    class Meta:
        unique_together=[['user_id','following_user_id']]

    def __str__(self):
        return (f"{self.user_id} is followed by {self.following_user_id}")


class InstaPost(models.Model):
    post_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=3) <= self.pub_date <= now

class Like(models.Model):
    post = models.ForeignKey(InstaPost, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(InstaPost, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comment_text

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
#cd /d C:/Users/sam/PycharmProjects/InstaClone
