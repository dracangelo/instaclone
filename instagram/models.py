from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime as dt
from PIL import Image

# # Create your models here.


class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)   
    image = models.ImageField(upload_to = 'ig/', null=False)
    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()
        return posts
    def save_post(self):
        self.save()
    def delete_post(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'ig/')
    caption = models.CharField(max_length=300)
    date_posted = models.DateField(default=timezone.now)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment = models.CharField(max_length=255)
    date_posted = models.DateField(default=timezone.now)
    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_photo = models.ImageField(default= 'levi.png', upload_to = 'ig/')
    bio = models.TextField(max_length=300)
    

    def __str__(self):
        return f'{self.user.username} Profile'

        
    def save_profile(self):
        self.save()

        profile_photo = Image.open(self.image.path)
        #To resize the profile image
        if image.height > 400 or image.width > 400:
            output_size = (400, 400)
            image.thumbnail(output_size)
            image.save(self.image.path)

    def delete_profile(self):
        self.delete()

    def updateProfile(sender, **kwargs):
        if kwargs['created']:
            profile = Profile.objects.created(user=kwargs['instance'])
            post_save.connect(Profile, sender=User)

    

