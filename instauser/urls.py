from django.urls import path
from instauser import views

app_name = "instauser"
urlpatterns = [
  path('login/', views.login_view, name= 'login'),

  ]