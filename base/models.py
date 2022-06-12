from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Profile(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('profile_photo', blank=True)
    bio = models.CharField(blank=True, max_length=150)
    facebook = models.URLField(blank=True, max_length=150)
    linkedln = models.URLField(blank=True, max_length=150)
    instagram = models.URLField(blank=True, max_length=150)
    twitter = models.URLField(blank=True, max_length=150)
    following = models.ManyToManyField('self', related_name='i_am_following', symmetrical=False, blank=True)
    followers = models.ManyToManyField('self', related_name='my_followers', symmetrical=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)



