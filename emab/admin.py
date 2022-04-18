from django.contrib import admin
from .models import Category, Toner, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Toner)
admin.site.register(Product)