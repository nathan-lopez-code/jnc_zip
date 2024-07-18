from django.contrib import admin
from .models import User, Archive, ChefProject, Building, Widgets

# Register your models here.
admin.site.register(User)
admin.site.register(Archive)
admin.register(Building)
admin.site.register(Widgets)

@admin.register(ChefProject)
class ChefProjetAdmin(admin.ModelAdmin):
    list_display = ('name','qualification')


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('address','construction_year','state')