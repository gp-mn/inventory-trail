from django.contrib import admin

# Register your models here.

# Allow admin page to access the model ItemGroup
from .models import ItemGroup
admin.site.register(ItemGroup)