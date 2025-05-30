# listings/models.py

from django.db import models
from django.utils import timezone # <--- Import timezone

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=timezone.now) # <--- Using timezone.now

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Listings" # <--- Makes the admin display "Listings" instead of "Listing"s