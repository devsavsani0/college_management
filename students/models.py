from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]

    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    department = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    admission_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.student_id} - {self.name}'
