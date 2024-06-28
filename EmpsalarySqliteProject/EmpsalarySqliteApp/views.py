from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salary_report')
    else:
        form = EmployeeForm()
        return render(request, 'EmpsalarySqliteApp/add_employee.html', {'form': form})
def salary_report(request):

    employees = Employee.objects.all()
    report = []
    for emp in employees:
        basic = emp.basic_salary
        da = basic * 0.80
        hra = basic * 0.15
        ma = basic * 0.10
        gross = basic + da + hra + ma
        report.append({
        'empno': emp.empno,
        'empname': emp.empname,
        'basic_salary': basic,
        'da': da,
        'hra': hra,
        'ma': ma,
        'gross_salary': gross
})
 # Print report to console
    for r in report:
        print(r)
    
    return render(request, 'EmpsalarySqliteApp/salary_report.html', {'report': report})

def home(request):
    return render(request, 'EmpsalarySqliteApp/home.html')