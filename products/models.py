from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


class Category(models.Model):
    """ Class to hold categories for products """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return str(self.name)


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


class Product(models.Model):
    """ Class to hold product information """
    sku = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    description = models.TextField()
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    sizes = MultiSelectField(choices=SIZE_CHOICES)
    ready_to_ship = models.BooleanField(default=False)

    def __str__(self):
        return str(self.friendly_name)


class Review(models.Model):
    """ Class to hold product reviews """

    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review"
    )
    name = models.CharField(max_length=254)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='review'
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField()

    def __str__(self):
        return f'Review by {self.name}'
