from django.db import models


class Faculty(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Faculty'
        ordering = ['name']

    def __str__(self):
        return f'{self.employee_id} - {self.name}'
