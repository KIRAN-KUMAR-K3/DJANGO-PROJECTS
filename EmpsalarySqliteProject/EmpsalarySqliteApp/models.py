from django.db import models
class Employee(models.Model):
    empno = models.IntegerField(unique=True)
    empname = models.CharField(max_length=100)
    basic_salary = models.FloatField()
    def __str__(self):
        return f"{self.empname} (Emp No: {self.empno})"