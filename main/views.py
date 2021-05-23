from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def showmain(request):
    post = Post.objects.all()
    return render(request, 'main/mainpage.html',{'post':post})
def first(request):
    return render(request, 'main/first.html')
def second(request):
    return render(request, 'main/second.html')
def detail(request,id):
    post = get_object_or_404(Post, pk = id)
    return render(request,'detail.html',{'post':post})    
def new(request):
    return render(request, 'main/new.html')
def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new.post.save()
    return redirect('detail',new_blog.id)