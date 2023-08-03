from django.contrib import admin

# Register your models here.

# Allow admin page to access the model ItemGroup
from .models import ItemGroup

class ItemGroupAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}
  
admin.site.register(ItemGroup, ItemGroupAdmin)