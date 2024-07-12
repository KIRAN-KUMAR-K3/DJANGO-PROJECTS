from django.db import models

class Student(models.Model):
    USN = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    semester = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_no = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=100)
    duration = models.DurationField()
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.course_name
