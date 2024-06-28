from django.contrib import admin
from .models import Book, Author, Publisher
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publisher', 'publication_date')
    ordering = ('publication_date',)
    search_fields = ('title',)
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher)