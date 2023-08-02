from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login_view, name='login'),  # login_view 뷰와 URL 매핑
    path('password/', views.password, name='password'),
    path('register/', views.register, name='register'),
    # 다른 뷰들과 URL 매핑 추가
]