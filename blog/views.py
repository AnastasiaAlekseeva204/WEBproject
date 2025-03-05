from django.shortcuts import render

# Create your views here.
def index(request):
    pass
def post_list(request):
    return render(request,'blog/post_list.html',{})
def post(request):
    return render(request,'blog/post.html',{})