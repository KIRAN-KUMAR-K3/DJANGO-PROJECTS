from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empno', 'empname', 'basic_salary']