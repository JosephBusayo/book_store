from django.db import models


class book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField()
    co_author = models.CharField(max_length=100)
    release = models.IntegerField()