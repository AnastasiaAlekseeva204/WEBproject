from django.shortcuts import render
from .models import Book
from .models import Category
from .models import Author
# Create your views here.

def main(request):
    books= Book.objects.all()
    authors = Author.objects.all().order_by("?")[:4]
    categorys = Category.objects.filter(parent__isnull=True).all()
    return render(request,'blog/main.html',{'books':books,'categorys':categorys,'authors': authors})

def book(request):
    book_id = request.GET.get('book_id')
    book = Book.objects.get(id=book_id)
    id_author = book.id_author
    author_simple_book = Book.objects.filter(id_author=id_author).exclude(id=book_id).all()
    id_category = book.category
    category_simple_book = Book.objects.filter(category=id_category).exclude(id=book_id).all()
    #category = Category.objects.get(id=cat_id)
    #books = Book.objects.filter(category=cat_id).all()
    #return render(request,'blog/book.html',{'books':books,'category':category})
    return render(request,'blog/book.html',{'book':book, 'author_simple_book':author_simple_book, 'category_simple_book':category_simple_book})

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

def allcategory(request):
    categorys = Category.objects.all().order_by("?")
    return render(request,'blog/allcategory.html',{'categorys':categorys})

def allauthor(request):
    authors = Author.objects.all()
    return  render(request,'blog/allauthor.html',{'authors':authors})
'''def base(request):
    return render(request,'blog/base.html')'''