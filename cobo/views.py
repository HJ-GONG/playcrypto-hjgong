from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

@login_required  # 로그인한 사용자만 접근 가능하도록 데코레이터 추가
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # 객체 생성을 지연시킴
            post.author = request.user  # 현재 로그인한 사용자를 작성자로 설정
            post.save()
            return redirect('cobo:board_list')  # 작성 완료 후 게시물 목록 페이지로 리디렉션
    else:
        form = PostForm()
    return render(request, 'cobo/post_create.html', {'form': form})

def board_list(request):
    posts = Post.objects.all()
    return render(request, 'cobo/board_list.html', {'posts': posts})

def post_detail(request):
    return render(request, 'cobo/post_detail.html')