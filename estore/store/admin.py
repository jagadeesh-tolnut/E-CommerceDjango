from django.contrib import admin

# Register your models here.
from .models import Product, Collection, Promotion

admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Promotion)