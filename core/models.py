from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    field_placement = models.ForeignKey('FieldPlacement', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')

class Supervisor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)

class FieldPlacement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='field_placements')
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length=100)
    feedback = models.TextField(blank=True, null=True)
