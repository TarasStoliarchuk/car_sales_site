from django.contrib import admin
from . import models


@admin.register(models.Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["salesperson", "name", "age", "create_at", "id"]
