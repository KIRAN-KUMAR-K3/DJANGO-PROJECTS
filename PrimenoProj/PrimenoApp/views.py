from django.shortcuts import render
from PrimenoApp.forms import NumberForm
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def prime_numbers(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            primes = [num for num in range(2, number + 1) if is_prime(num)]
            return render(request, 'PrimenoApp/result.html', {'number': number, 'primes': primes})
    else:
        form = NumberForm()
    return render(request, 'PrimenoApp/index.html', {'form': form})