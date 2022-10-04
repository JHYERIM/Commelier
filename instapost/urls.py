from django.urls import path, include
from . import views

app_name = 'instapost'
urlpatterns = [
  #20220930 박소민 
    path('index/', views.index, name= 'index'),
    path('new_post/', views.create_post, name= 'create_review'), #new_post -> create_post로 변경 (22.09.30 문규빈)
    
    # 221004 박소민 게시글 상세페이지 추가
    path('instapost/<int:id>', views.detail_post, name= 'detail_post'),
    
    # 221004 박소민 댓글 create url 추가
    # 여기서 달린 <int:id>는 instapost의 pk입니다.
    path('comment/<int:id>', views.create_comment, name= 'create_comment'),
    
    # 221004 최해민 댓글 delete url 추가
    path('comment/delete/<int:id>', views.delete_comment, name= 'delete_comment'),
]
