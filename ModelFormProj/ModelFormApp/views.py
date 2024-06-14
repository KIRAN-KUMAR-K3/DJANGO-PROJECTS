from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            #print("Form is valid and saved. Now printing books to console.")
            #print_books_to_console() # Call function to print books
            return redirect('book_success')
        #else:
            #print("Form is not valid.")
    else:
        print("Request method is not POST.")
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})
def book_success_view(request):
    return render(request, 'book_success.html')
def home_view(request):
    return render(request, 'home.html')