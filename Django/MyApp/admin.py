from django.contrib import admin
from MyApp.models import Pet

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass