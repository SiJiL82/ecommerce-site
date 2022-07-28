from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
  """ A class to hold review information """

  user_id = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="review"
  )
  name = models.CharField(max_length=254)
  product = models.ForeignKey (
    Product, on_delete=models.CASCADE, related_name='review'
  )
  rating = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
  date = models.DateTimeField(auto_now_add=True)
  review = models.TextField()

  def __str__(self):
    return f'Review by {self.name}'
