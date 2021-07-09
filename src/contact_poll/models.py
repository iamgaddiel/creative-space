from django.db import models
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    state = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=timezone.now)


    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.timestamp}"

