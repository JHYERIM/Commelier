from distutils.command.upload import upload
from django.db import models
import instapost
from instauser.models import InstaUser



# Create your models here.

class Instapost(models.Model): #메인페이지 클래스 생성
    content = models.TextField(max_length=100)
    # image = models.ImageField # 이건 이미지가 딱 하나 업로드할 수 있습니다.
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(InstaUser, on_delete=models.CASCADE)
    

class Image(models.Model): # 게시물 목록/ 게시물 작성에 들어갈 이미지 업로드 클래스 생성
    image = models.ImageField(blank =True ,null=True ,upload_to='images') 
    instapost = models.ForeignKey(Instapost, on_delete=models.CASCADE, related_name='images')
    #image를 ImageField를 이용해 imges라는 디렉토리 아래에 업로드

    
class Edit_time(models.Model):
    modify_date =models.DateTimeField(null=True,blank=True)

#2022.10.03 class가 하나만 있어도 될 것 같아서 posting class 삭제
#image -foreign key 

# 221004 박소민, 최해민 댓글 클래스 생성
class InstaComment(models.Model):
    content = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(InstaUser, on_delete=models.CASCADE)
    instapost = models.ForeignKey(Instapost, on_delete=models.CASCADE, related_name='comments')
