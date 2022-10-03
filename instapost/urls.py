# 221003 최해민 urls.py 생성

from django.urls import path, include
from instapost import views

# 220930 최해민 앱네임 추가
app_name = 'instapost'
urlpatterns = [
    path('post/', views.post, name='post'),
    path('detail_page/', views.detail_page, name='detail_page'),
]
