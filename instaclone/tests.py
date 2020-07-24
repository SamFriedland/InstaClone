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

class UserFollowTests(TestCase):

    def setUp(self):
        user_one=User.objects.create(username="user_one")
        user_two=User.objects.create(username="user_two")
        UserFollowing.objects.create(user_id=user_one, following_user_id=user_two)

    def test_user_follows_user(self):
        self.assertQuerysetEqual(
            UserFollowing.objects.all(),
            ['<UserFollowing: user_one is followed by user_two>']
        )

    def test_following(self):
        user_one = User.objects.get(username="user_one")
        self.assertQuerysetEqual(user_one.followers.all(), ['<UserFollowing: user_one is followed by user_two>'])

    def test_followers(self):

        user_two = User.objects.get(username="user_one")
        self.assertQuerysetEqual(user_two.following.all(),['<UserFollowing: user_one is followed by user_two>'])