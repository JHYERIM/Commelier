"""Commelier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#20220930 박소민 
from instapost import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 220930 최해민 회원가입 기능을 구현을 위해 instauser url로 보내주기
    path('', include('instauser.urls')),
    
    # 221003 최해민 comment 기능 추가
    path('', include('instapost.urls')),
    
    #20220930 박소민 
    path('index/', views.index),
    path('new_post/', views.create_post), #new_post -> create_post로 변경 (22.09.30 문규빈)
]
