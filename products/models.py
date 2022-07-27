from django.db import models

class Category(models.Model):
  """ Class to hold categories for products """

  class Meta: 
    verbose_name_plural = 'Categories'

  name = models.CharField(max_length=254)
  friendly_name = models.CharField(max_length=254)

  def __str__(self):
    return str(self.name)
