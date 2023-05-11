from django.db import models


# Create your models here.
class Book(models.Model):
    tite = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    summary = models.CharField(max_length=255

class Genre(models.Model):
    name=models.CharField(max_length=55)

class language(models.Model):
    name = models.CharField(max_length=255)

class BookInstance(models.Model):
    STATUS_CHOICES =[
        ('RETURNED','R'),
        ('BORROWED','B')
    ]
    due_black = models.DateField()
    status=models.CharField(max_length=1, choices=STATUS_CHOICES)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    imprint=models.CharField(max_length=55)
    borrower=""

class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_birth = models.DateField()
