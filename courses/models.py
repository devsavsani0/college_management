from django.db import models
from faculty.models import Faculty


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150)
    department = models.CharField(max_length=100)
    credits = models.PositiveSmallIntegerField(default=3)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')

    class Meta:
        ordering = ['code']

    def __str__(self):
        return f'{self.code} - {self.name}'
