from django.shortcuts import render
from .models import Book
from .models import Category
from .models import Author
from .forms import SearchForm
from django.db.models import Q
from .models import New
# Create your views here.

def main(request):
    books= Book.objects.all()
    authors = Author.objects.all().order_by("?")[:4]
    categorys = Category.objects.filter(parent__isnull=True).all()
    news= New.objects.all().order_by("-cur_date")[:2]
    popularbook = Book.objects.filter(count_view__gt=5).all().order_by("-count_view")[:4]
    return render(request,'blog/main.html',{'books':books,'categorys':categorys,'authors': authors,'news':news,'popularbook':popularbook})

def book(request):
    book_id = request.GET.get('book_id')
    book = Book.objects.get(id=book_id)
    if book.count_view:
        book.count_view+=1
    else:
        book.count_view=1
    book.save()
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
    categorys = Category.objects.all().order_by("title")
    return render(request,'blog/allcategory.html',{'categorys':categorys})

def allauthor(request):
    authors = Author.objects.all()
    return  render(request,'blog/allauthor.html',{'authors':authors})
'''def base(request):
    return render(request,'blog/base.html')'''

def popularbook(request):
    popularbook = Book.objects.filter(count_view__gt=5).all().order_by("-count_view")
    return render(request,'blog/popularbook.html',{'popularbook':popularbook})

def aboutus(request):
    aboutus = Author.objects.all()
    return render(request,'blog/aboutus.html',{'aboytus':aboutus})

def search(request):
    searchform = SearchForm()
    results = ""
    if "query" in request.GET:
        searchform = SearchForm(request.GET)
        if searchform.is_valid():
            cd = searchform.cleaned_data
            results = Book.objects.filter(Q(title__iregex=cd['query'] ) | Q(content__iregex=cd['query']) | Q(id_author__title__iregex=cd['query'])).all()
    return render(request,'blog/forms.html',{'searchform': searchform, 'results': results})

def allnews(request):
    news = New.objects.filter(enabled=1).all().order_by("-cur_date")
    return render(request,'blog/allnews.html',{'news': news})

def new(request):
    new_id = request.GET.get('new_id')
    new= New.objects.get(id=new_id)
    return render(request,'blog/new.html',{'new':new})