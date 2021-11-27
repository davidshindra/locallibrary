from django.contrib import admin

from .models import Author, Category, Book, BookCopy, Language

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    pass
