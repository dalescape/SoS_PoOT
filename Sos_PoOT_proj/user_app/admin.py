from django.contrib import admin
from .models import User # I added this

# Register your models here.

admin.site.register([User])   # I added this