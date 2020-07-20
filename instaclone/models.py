from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64)
    email
    date_of_birth
    profile_pic
    bio

    def __str__(self):
        return self.username


class Follows(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    def __str__(self):
        return ("f' {self.User} is followed by {following]")


class Instapost(models.Model):
    post_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

class Like(models.Model):
    post = models.ForeignKey(Instapost, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Instapost, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comment_text

#cd /d C:/Users/sam/PycharmProjects/InstaClone
