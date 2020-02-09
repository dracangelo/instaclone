from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='avatar/', blank=True)
    bio = models.CharField(max_length=30, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    following = models.ManyToManyField(User, blank=True, related_name='followed_by')

    

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.user.username)

    def __str__(self):
        return self.first_name

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def get_searched_profile(cls, search_term):
        profiles = cls.objects.filter(first_name__icontains=search_term)
        return profiles

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()



class Image(models.Model):
    pic = models.ImageField(upload_to='images/', blank=True)
    caption = models.CharField(max_length=60, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.caption
    def get_number_of_likes(self):
        return self.like_set.count()

    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    image = models.ForeignKey(Image, null=True)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment


class Like(models.Model):
    image = models.ForeignKey(Image, null=True)
    user = models.ForeignKey(User)

    # class Meta:
    #     unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title