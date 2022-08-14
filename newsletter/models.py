from django.db import models


class Newsletter(models.Model):
    """ Class to hold newsletter subscriber info """

    full_name = models.CharField(max_length=254, blank=False, null=False)
    email = models.CharField(max_length=254, blank=False, null=False)
