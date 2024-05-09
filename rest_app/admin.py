from django.contrib import admin
from rest_app.models import Category, Product


@admin.register(Product)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']


@admin.register(Category)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']
