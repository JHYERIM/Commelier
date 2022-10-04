from turtle import update
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'instapost'
urlpatterns = [
  #20220930 박소민 
    path('index/', views.index, name= 'index'),
    path('new_post/', views.create_post, name= 'create_review'), #new_post -> create_post로 변경 (22.09.30 문규빈)
    path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('<int:pk>/update/', views.update, name = 'update'),
    path('<int:pk>/update/edit', views.remove_post, name = 'remove'),

    # 221004 박소민 게시글 상세페이지 추가
    path('instapost/<int:id>', views.detail_post, name= 'detail_post'),
    
    # 221004 박소민 댓글 create url 추가
    # 여기서 달린 <int:id>는 instapost의 pk입니다.
    path('comment/<int:id>', views.create_comment, name= 'create_comment'),
    
    # 221004 최해민 댓글 delete url 추가
    path('comment/delete/<int:id>', views.delete_comment, name= 'delete_comment'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

