from django.core.management.base import BaseCommand
from ModelFormApp.models import Book
class Command(BaseCommand):
    help = 'Prints all books in the database'
    def handle(self, *args, **kwargs):
        books = Book.objects.all()
        self.stdout.write("Printing books to console:")
        for book in books:
            self.stdout.write(f"Title: {book.title}, Author: {book.author}, Published Date:{book.published_date}, ISBN: {book.isbn}, Pages: {book.pages}")