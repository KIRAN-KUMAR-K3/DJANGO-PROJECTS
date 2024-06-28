from django.shortcuts import render
from .forms import StringConverterForm
def string_converter_view(request):
    result = None
    if request.method == 'POST':
        form = StringConverterForm(request.POST)
        if form.is_valid():
            input_string = form.cleaned_data['input_string']
            case_choice = form.cleaned_data['case_choice']
            if case_choice == 'upper':
                result = input_string.upper()
            elif case_choice == 'title':
                result = input_string.title()
            elif case_choice == 'lower':
                result = input_string.lower()
            elif case_choice == 'sentence':
                result = input_string.capitalize()
    else:
        form = StringConverterForm()
    return render(request, 'StringConverterApp/converter.html', {'form': form, 'result': result})

from django.http import HttpResponse
def quit_view(request):
    return HttpResponse("Thank you for using the string converter. You can close this window.")