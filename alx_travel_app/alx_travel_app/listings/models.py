from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

class Listing(models.Model):
    # Basic Listing Information
    title = models.CharField(max_length=200, default='') # Added default
    address = models.CharField(max_length=200, default='') # Added default
    city = models.CharField(max_length=100, default='') # Added default
    state = models.CharField(max_length=100, default='') # Added default
    zipcode = models.CharField(max_length=20, default='') # Added default
    description = models.TextField(blank=True)

    # Numerical Listing Details
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0) # Added default
    bedrooms = models.IntegerField(default=0) # Added default
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, default=0.0) # Added default
    sqft = models.IntegerField(default=0) # Added default
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, default=0.0) # Added default

    # Media and Status
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.user.username}"


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('listing', 'user')

    def __str__(self):
        return f"Review for {self.listing.title} by {self.user.username} - {self.rating} stars"