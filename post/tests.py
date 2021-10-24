from django.contrib.auth.models import User
from django.test import TestCase
from authy.models import Profile
from post.models import Post

# Create your tests here.
class TestPost(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='roy')
        self.profile_test.save()

        self.image_test = Post(image='default.png', name='test', caption='default test', user=self.profile_test)

    def test_insatance(self):
        self.assertTrue(isinstance(self.image_test, Post))

    def test_save_image(self):
        self.image_test.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)