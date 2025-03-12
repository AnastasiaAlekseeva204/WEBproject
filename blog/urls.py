from django.urls import path 
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('book',views.book,name='book'),
    path('author',views.author,name='author'),
    path('category',views.category,name='category')
]