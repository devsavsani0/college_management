from django.contrib import admin
from .models import Faculty

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department', 'designation')
    search_fields = ('employee_id', 'name', 'email')
