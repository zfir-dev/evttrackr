from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, default='Draft')

    def __str__(self):
        return self.name
