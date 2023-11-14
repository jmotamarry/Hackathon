from django.db import models

# Create your models here.

class Event(models.Model):  # makes an event class with five atributes
    title = models.TextField()
    description = models.TextField()
    date = models.TextField()
    time = models.TextField(default='')
    posting_club = models.TextField()
