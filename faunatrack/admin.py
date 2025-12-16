from django.contrib import admin

from faunatrack.models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_editable = ["name"]