from django.db import models

class Event(models.Model):
  """ A class to hold calendar events """

  location_name = models.CharField(max_length=254)
  location_address = models.TextField()
  date = models.DateField()
  start_time = models.TimeField()
  end_time = models.TimeField()
  description = models.TextField()

  def __str__(self):
    return self.location_name
