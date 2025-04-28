from django.db import models
from django.contrib.auth.models import User  # This is necessary for the Room model

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
