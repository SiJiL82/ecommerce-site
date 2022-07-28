from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
  """ A class to hold a customer product request """
  SIZE_CHOICES = (
    ('6-9m', '6-9 months'),
    ('9-12m', '9-12 months'),
    ('12-18m', '12-18 months'),
    ('18-24m', '18-24 months'),
    ('2-3y', '2-3 years'),
    ('3-4y', '3-4 years'),
    ('4-5y', '4-5 years'),
    ('5-6y', '5-6 years'),
    ('6-7y', '6-7 years'),
    ('7-8y', '7-8 years'),
    ('8-9y', '8-9 years'),
    ('9-10y', '9-10 years'),
  )
  user_id = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="request")
  name = models.CharField(max_length=254)
  email_address = models.EmailField()
  category = models.ForeignKey('products.Category', null=True, blank=True, on_delete=models.SET_NULL)
  size = models.CharField(
    max_length=254,
    choices = SIZE_CHOICES
  )
  description = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)
  fulfilled = models.BooleanField(default=False)

  def __str__(self):
    return f'Request from {self.name}'
