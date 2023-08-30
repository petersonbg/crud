from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.home, name='index'),
    path('create_books/', views.create_books, name='create'),
    path('list_books/', views.list_books, name='books'),
    path('views_book/<int:livro_id>/', views.view_book, name='view_book'),
    path('edit_book/<int:livro_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:livro_id>/', views.delete_book, name='delete_book'),
    path('create_categories/', views.create_categories, name='create_categories')
]