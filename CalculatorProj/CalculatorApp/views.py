from django.shortcuts import render
from django.http import HttpResponse

from .forms import CalculatorForm
def calculator_view(request):
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            operation = form.cleaned_data['operation']
            if operation == 'add':
                result = number1 + number2
            elif operation == 'subtract':
                result = number1 - number2
            elif operation == 'multiply':
                result = number1 * number2
            elif operation == 'divide':
                if number2 != 0:
                    result = number1 / number2
                else:
                    result = 'Error: Division by zero'
            elif operation== 'moddiv':
                result=number1 % number2
    else:
        form = CalculatorForm()
    return render(request, 'CalculatorApp/calculator.html', {'form': form, 'result': result})


def quit_view(request):
    return HttpResponse("Thank you for using the calculator. You can close this window.")