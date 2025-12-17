from django.contrib import admin
from .models import Espece, Location, ProfilScientifique, Project, Observation, ProjectMembership


# https://unfoldadmin.com/docs/integrations/django-celery-beat/@admin.register(Espece)
# Utilisr les modèles 'Inlines' pour améliorer l'UX/UI

@admin.register(Espece)
class EspeceAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'created_at', 'updated_at']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'latitude', 'longitude', 'created_at', 'updated_at']
    
class ObservationInline(admin.TabularInline):
    extra = 1
    model = Observation
    

class ProjectMembershipInline(admin.TabularInline):
    model = ProjectMembership
    extra = 1
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'titre', 'description', 'created_at', 'updated_at']
    inlines = [ObservationInline, ProjectMembershipInline]

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'location', 'date_observation', 'created_at', 'updated_at']
    list_filter = ['project', 'location', 'date_observation']


class MembershipInline(admin.TabularInline):
    model = ProjectMembership
    extra = 1
@admin.register(ProfilScientifique)
class ScientifiqueAdmin(admin.ModelAdmin):
    list_display = ["user__email", "user__username"]
    inlines = [MembershipInline]
    search_fields = ['user__email', 'user__username']
