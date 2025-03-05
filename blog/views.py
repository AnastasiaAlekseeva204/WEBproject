from django.shortcuts import render
from .models import Book
# Create your views here.

def post(request):
    books= Book.objects.all()
    return render(request,'blog/post.html',{'books':books})