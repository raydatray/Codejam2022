from django.contrib import admin
from .models import listing, User

# Register your models here.

admin.site.register(listing)
admin.site.register(User)
