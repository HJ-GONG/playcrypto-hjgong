# from django.shortcuts import render

# def login(request):
#     return render(request, 'account/login.html')

# def password(request):
#     return render(request, 'account/password.html')

# def register(request):
#     return render(request, 'account/register.html')

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User

def login(request):
    return render(request, 'account/login.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 사용자를 로그인 상태로 만듦
            return redirect("/playcrypto/")  # 로그인 성공 시 리다이렉션 또는 원하는 처리 로직
        else:
            # 로그인 실패 시 에러 메시지 또는 원하는 처리 로직
            return render(request, "account/login.html", {"error_message": "로그인 실패"})
    else:
        return render(request, "account/login.html")

def password(request):
    return render(request, 'account/password.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return redirect('account:login')
        else:
            # Handle password mismatch error
            return render(request, 'account/register.html', {'error': 'Passwords do not match'})

    return render(request, 'account/register.html')

@login_required  # 로그인한 사용자만 접근 가능하도록 데코레이터 추가
def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        # 현재 로그인한 사용자를 작성자로 설정
        post = Post.objects.create(title=title, content=content, author=request.user)
        return redirect('post_detail', post_id=post.id)
    else:
        return render(request, 'post_create.html')