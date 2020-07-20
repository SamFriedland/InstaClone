from django.db import models

# Create your models here.
def#
class User(models.Model):
    username = models.CharField(max_length=30)

class Followers(models.Model):
    followers = models.ForeignKey(User, on_delete=models.CASCADE)

class Following(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE)
class Instapost(models.Model):
    post_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title



class Like(models.Model):
    post = models.ForeignKey(Instapost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):d
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Instapost, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comment_text



