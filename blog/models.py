from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Book(models.Model):
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    book_desc = models.TextField()
    book_img = models.ImageField(upload_to='bookimage', max_length=200, null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    class META:
        ordering = ['-create_on']

    def __str__(self):
        return self.book_title
        
    

class Comment(models.Model):
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)    
    comment_on = models.DateTimeField(auto_now_add=True)
    comment_update_on = models.DateTimeField(auto_now=True)


class LikeBook(models.Model):
    like_by = models.ForeignKey(User, on_delete=models.CASCADE)
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
