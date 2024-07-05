# views.py in FeedbackApp
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'FeedbackApp/contact.html', {'form': form})

def success(request):
    return render(request, 'FeedbackApp/success.html')
