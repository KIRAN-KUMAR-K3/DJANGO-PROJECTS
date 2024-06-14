from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from .forms import NumberCheckForm
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "It is not a Prime number"
    return "It is a prime number"

def is_even(n):
    return "It is an even number" if n % 2 == 0 else "It is not an even number"

def is_odd(n):
    return "It is an odd number" if n % 2 != 0 else "It is not an odd number"

def is_perfect_square(n):
    return "It is a perfect square" if math.sqrt(n) ** 2 == n else "It is not a perfect square"

def index(request):
    result = {}
    if request.method == 'POST':
        form = NumberCheckForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            if form.cleaned_data['is_prime']:
                result['is_prime'] = is_prime(number)
            if form.cleaned_data['is_even']:
                result['is_even'] = is_even(number)
            if form.cleaned_data['is_odd']:
                result['is_odd'] = is_odd(number)
            if form.cleaned_data['is_perfect_square']:
                result['is_perfect_square'] = is_perfect_square(number)
    else:
        form = NumberCheckForm()
    return render(request, 'NumberCheckerApp/index.html', {'form': form, 'result': result})