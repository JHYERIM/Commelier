from distutils.command.upload import upload
from django.db import models
from instauser.models import InstaUser



# Create your models here.

class Instapost(models.Model):
    content = models.TextField(max_length=100)
    # image = models.ImageField # 이건 이미지가 딱 하나 업로드할 수 있습니다.
    create_date = models.DateTimeField(auto_now_add=True)
    nickname = models.ForeignKey(InstaUser, on_delete=models.CASCADE)
# author
# 내지는 user?, instauser
# InstaUser 안에 있는 "최해민" 이라는 사람들 데려올거잖아용
# 최해민이라는 사람의 닉네임을 갖다 쓰면 되니까
# 굳이 nickname이라 적어줄 필요 없읍니다.
# 게시글은 작성자만 있으면 대겠져?

class Image(models.Model):
    image = models.ImageField(upload_to='ssum')




