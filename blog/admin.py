from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ["book_title", "create_by", "book_desc", "book_img", 'create_on', 'id']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["comment_by", "bookid", "comment", "comment_on", 'id']

@admin.register(LikeBook)
class LikeBookAdmin(admin.ModelAdmin):
    list_display = ["bookid", "like", "like_by"]
