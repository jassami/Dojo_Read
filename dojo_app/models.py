from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField



class Author(models.Model):
    name= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title= models.CharField(max_length=255)
    user= models.ForeignKey('login_app.User', related_name="books", on_delete=models.CASCADE)
    author= models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

class Review(models.Model):
    review= models.TextField()
    rating= models.IntegerField()
    user= models.ForeignKey('login_app.User', related_name="reviews", on_delete=models.CASCADE)
    book= models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
