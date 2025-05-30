from django.contrib import admin

# Register your models here.
from .models import Listing # <--- Import your Listing model

admin.site.register(Listing) # <--- Register the model