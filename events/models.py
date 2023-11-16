from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Event(models.Model):                                      # makes the main data model, each event has the attributes below
    title        = models.CharField(max_length=120)
    description  = models.TextField(blank=True, default='')
    repeats      = models.BooleanField(default=False)
    approved     = models.BooleanField(default=False)
    date         = models.DateField()
    start_time   = models.TimeField()
    end_time     = models.TimeField()
    posting_club = models.CharField(max_length=100)
    user         = models.ForeignKey(to=User, related_name="events", blank=True, null=True, on_delete=models.CASCADE)
    image        = models.ImageField(null=True, blank=True, upload_to='images/')

    def get_absolute_url(self):
        return reverse('events:event', kwargs={'id': self.id})