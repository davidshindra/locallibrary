from uuid import uuid4

from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Create your models here.

class Language(models.Model):

    language_id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Category(models.Model):

    category_id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Author(models.Model):

    author_id = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=60)       
    last_name = models.CharField(max_length=60)
    other_names = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    date_of_birth = models.DateField()       
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' 

    def save(self, *args, **kwargs):
        # todo create a slug that will guranttee uniqueness of authors with the same names 
        if not self.slug:
            self.slug = slugify(f'{self.first_name} {self.last_name}')
        super().save(*args, **kwargs)

    @property
    def fullname(self):
        if self.other_names:
            return f'{self.first_name} {self.other_names} {self.last_name}'
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):

    book_id = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, related_name='books') 
    summary = models.TextField(max_length=1000)
    ISBN = models.CharField(max_length=13, verbose_name='ISBN', unique=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BookCopy(models.Model):

    User = get_user_model()
    BOOK_STATUS_CHOICES = [
        ('Available', 'Available'),
        ('OnLoan', 'OnLoan'),
        ('Reserved', 'Reserved'),
        ('Maintainance', 'Maintainance')
    ]

    book_copy_id = models.UUIDField(primary_key=True, default=uuid4)
    borrower = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='borrowed_books')
    status = models.CharField(max_length=12, choices=BOOK_STATUS_CHOICES, default='Maintainance')
    due_back = models.DateField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, related_name='copies')

    class Meta:
        ordering = ['-due_back']
        verbose_name_plural = 'book copies'