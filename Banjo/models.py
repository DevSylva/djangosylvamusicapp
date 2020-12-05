from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class YoutubeFeed(models.Model):
    description = models.CharField(max_length=100, null=False, blank=True)
    image = models.ImageField(null=True, blank=True)
    link = models.CharField(max_length=1000, null=False, blank=True)

    def __str__(self):
        return self.description

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Music(models.Model):
    title = models.CharField(max_length=30, null=False, blank=True)
    artist = models.CharField(max_length=50, null=False, blank=True)
    file_location = models.ImageField(null=True, blank=True, verbose_name="Music file directory")

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    comment = models.CharField(max_length=1000, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    image = models.ImageField(null=True, blank=True)
    tag = models.CharField(max_length=50, null=False, blank=True)
    link = models.CharField(max_length=250, null=False, blank=True)

    def __str__(self):
        return self.tag

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Event(models.Model):
    name = models.CharField(max_length=30, null=False, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.CharField(max_length=20, null=False, blank=True)
    event = models.CharField(max_length=60, null=False, blank=True)
    location = models.CharField(max_length=50, null=False, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class ContactInfo(models.Model):
    email = models.EmailField(max_length=150, null=False, blank=True)
    phoneNumber = models.CharField(max_length=20, null=False, blank=True)
    address = models.CharField(max_length=30, null=False, blank=True)
    hotline = models.CharField(max_length=20, null=False, blank=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    email = models.EmailField(max_length=200, null=False, blank=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

