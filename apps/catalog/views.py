from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from .models import Author, Book, BookCopy, Category

# Create your views here.

class HomeView(View):
    def get(self, request):
        num_authors = Author.objects.all().count()
        num_books = Book.objects.all().count()
        num_copies = BookCopy.objects.all().count()
        num_copies_available = BookCopy.objects.filter(status__iexact='Available')
        num_categories = Category.objects.all().count()
        context = {
            'num_authors': num_authors,
            'num_books': num_books,
            'num_copies': num_copies,
            'num_copies_available': num_copies_available,
            'num_categories': num_categories
        }
        return render(request, 'catalog/home.html', context)