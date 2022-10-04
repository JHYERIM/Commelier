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

    # path('detail_page_1/<int:pk>/', views.post_Edit, name= 'datail_page'),
    # path('detail_page_1/<int:pk>/delete/', views.remove_post, name= 'datail_delete'),
    # path('detail_page_1/<int:pk>/modify/', views.post_modify, name= 'datail_modiif'),

    path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('<int:pk>/update/', views.update, name = 'update'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

