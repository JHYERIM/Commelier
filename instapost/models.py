from distutils.command.upload import upload
from django.db import models
from instauser.models import InstaUser



# Create your models here.

class Instapost(models.Model): #메인페이지 클래스 생성
    content = models.TextField(max_length=100)
    # image = models.ImageField # 이건 이미지가 딱 하나 업로드할 수 있습니다.
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(InstaUser, on_delete=models.CASCADE)


class Image(models.Model): # 게시물 목록/ 게시물 작성에 들어갈 이미지 업로드 클래스 생성
    image = models.ImageField(upload_to='ssum')
