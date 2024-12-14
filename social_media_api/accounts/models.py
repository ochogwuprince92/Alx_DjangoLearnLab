from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name= 'following')

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    # Add a many-to-many relationship for the following functionality
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)

    def __str__(self):
        return self.username