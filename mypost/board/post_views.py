from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Member

def index (request) :
    posts = Post.objects.all()      #모든 post 데이터 불러오기
    context = {                     #템플릿으로 전달
        'posts' : posts,    
    }

    return render(request,'index.html',context)
# Create your views here.
