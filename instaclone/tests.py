from django.test import TestCase
from django.utils import timezone
from .models import User,UserFollowing,InstaPost,Like,Comment,CommentLike
import datetime
from django.urls import reverse

# Create your tests here.
class InstaPostTests(TestCase):
    def test_was_published_recently(self):
        time=timezone.now() - datetime.timedelta(days=2, hours=23)
        recentPost = InstaPost(pub_date=time)
        self.assertIs(recentPost.was_published_recently(), True)

    def test_was_published_far_in_past(self):
        time=timezone.now() - datetime.timedelta(days=3, seconds=1)
        oldPost = InstaPost(pub_date=time)
        self.assertIs(oldPost.was_published_recently(), False)

