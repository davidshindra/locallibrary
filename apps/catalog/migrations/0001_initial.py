# Generated by Django 3.2.9 on 2021-11-25 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('other_names', models.CharField(blank=True, max_length=120, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('summary', models.TextField(max_length=1000)),
                ('ISBN', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='books', to='catalog.author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('book_copy_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('OnLoan', 'OnLoan'), ('Reserved', 'Reserved'), ('Maintainance', 'Maintainance')], default='Maintainance', max_length=12)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='copies', to='catalog.book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='borrowed_books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'book copies',
                'ordering': ['-due_back'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='catalog.Category'),
        ),
    ]
