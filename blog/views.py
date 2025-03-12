from django.shortcuts import render
from .models import Book
from .models import Category
from .models import Author
# Create your views here.

def main(request):
    books= Book.objects.all()
    authors = Author.objects.all()
    categorys = Category.objects.filter(parent__isnull=True).all()
    return render(request,'blog/main.html',{'books':books,'categorys':categorys,'authors': authors})

def book(request):
    book_id = request.GET.get('book_id')
    #category = Category.objects.get(id=cat_id)
    #books = Book.objects.filter(category=cat_id).all()
    #return render(request,'blog/book.html',{'books':books,'category':category})
    return render(request,'blog/book.html',{})

def author(request):
    author_id = request.GET.get('author_id')
    author=Author.objects.get(id=author_id)
    books = Book.objects.filter(id_author=author_id).all()
    return render(request,'blog/author.html',{'books':books,'author':author})

def category(request):
    cat_id = request.GET.get('cat_id')
    category = Category.objects.get(id=cat_id)
    books = Book.objects.filter(category=cat_id).all()
    return render(request,'blog/category.html',{'books':books,'category':category})