from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'department', 'year', 'status')
    search_fields = ('student_id', 'name', 'email')
    list_filter = ('department', 'year', 'status')
