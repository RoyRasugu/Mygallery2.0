from django.db import models
from django.contrib.auth.models import User
from post.models import Post

from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

from PIL import Image
from django.conf import settings
import os

# Create your models here.

# def user_directory_path(instance, filename):
#     # this file will be uploaded to MEDIA_ROOT /user(id)/filename
# 	profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
# 	full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

# 	if os.path.exists(full_path):
# 		os.remove(full_path)

# 	return profile_pic_name

class Profile(models.Model):
	'''
    this is a model class that defines how a user profile will be created
    '''
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	first_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	location = models.CharField(max_length=50, null=True, blank=True)
	profile_info = models.TextField(max_length=150, null=True, blank=True)
	created = models.DateField(auto_now_add=True)
	favorites = models.ManyToManyField(Post)
	pic = CloudinaryField('photo', null=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		SIZE = 300, 300

		if self.picture:
			pic = Image.open(self.picture.path)
			pic.thumbnail(SIZE, Image.LANCZOS)
			pic.save(self.picture.path)
		

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)