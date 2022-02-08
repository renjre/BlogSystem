from django.contrib import admin
from django.urls import path, include
from blog import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('createpost/', views.book, name='createpost'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('book/<int:id>/', views.seebook, name='seebook'),

    path('deletecomm/<int:id>', views.delete_comment, name='commdelete'),
    path('updatecomm/<int:id>', views.update_comment, name='updatecomm'),

    path('delete/<int:id>', views.delete_book, name='delete'),
    path('update/<int:id>', views.update_book, name='update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)