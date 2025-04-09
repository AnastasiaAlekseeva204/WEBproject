from django.urls import path 
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('book',views.book,name='book'),
    path('author',views.author,name='author'),
    path('category',views.category,name='category'),
    path('allcategory',views.allcategory,name='allcategory'),
    path('allauthor',views.allauthor,name='allauthor'),
    path('popularbook',views.popularbook,name='popularbook'),
    path('aboutus',views.aboutus,name='aboutus')
    #path('base',views.base,name='base')
]