from django.db import models

# Create your models here.

class Event(models.Model):  # makes an event class with five atributes
    title        = models.CharField(max_length=120) # make title limited to 120 chars
    description  = models.TextField(blank=True, default='') # make description not required
    date         = models.DateField()
    repeats      = models.BooleanField()
    start_time   = models.TimeField()
    end_time     = models.TimeField(blank=True) # make end time not required
    posting_club = models.CharField(max_length=100)
