from django.db import models
from django.urls import reverse


# Create your models here.

class Event(models.Model):  # makes an event class with five atributes
    title        = models.CharField(max_length=120) # make title limited to 120 chars
    description  = models.TextField(blank=True, default='') # make description not required
    repeats      = models.BooleanField(default=False)
    approved     = models.BooleanField(default=False)
    date         = models.DateField()
    start_time   = models.TimeField()
    end_time     = models.TimeField()
    posting_club = models.CharField(max_length=100)
    upload       = models.ImageField(upload_to='events/static', default='', blank=True)

    def get_absolute_url(self):
        return reverse('events:event', kwargs={'id': self.id})
