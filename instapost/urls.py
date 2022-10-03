from django.urls import path, include
from . import views

app_name = 'instapost'
urlpatterns = [
  #20220930 박소민 
    path('index/', views.index, name= 'index'),
    path('new_post/', views.create_post, name= 'create_review'), #new_post -> create_post로 변경 (22.09.30 문규빈)
]