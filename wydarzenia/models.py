from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Topic(models.Model):
    objects = None
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Room(models.Model):
    objects = None
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(default="", max_length=50)


class Meta:
    ordering = ["-updated", "-created"]

    def __init__(self):
        self.name = None

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # body = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    date = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.body[0:50]
