from django.contrib import admin
from .models import Espece, Location, Project, Observation

@admin.register(Espece)
class EspeceAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'created_at', 'updated_at']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'latitude', 'longitude', 'created_at', 'updated_at']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'titre', 'description', 'created_at', 'updated_at']

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'location', 'date_observation', 'created_at', 'updated_at']


