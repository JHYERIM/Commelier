# 221003 최해민 import redirect 추가
from django.shortcuts import render, redirect
from .models import Instapost,Image


# Create your views here.
def index(request):
    return render(request, 'index.html')

# 220930 박소민, 문규빈, 장혜림 포스트생성 함수 추가가
def create_post(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            return render(request, 'new_post.html')
        else:  # 로그인이 되어 있지 않다면
            return redirect('/login/')
        
    elif request.method == 'POST': #요청하는 방식이 POST 방식인지 확인
        user = request.user #현재 로그인 한 사용자를 불러오기
        print(user)
        new_post = Instapost( ) #글쓰기 모델 가져오기
        new_image = Image( ) 
        # 게시물의 작성자 = 현재 요청하는 유저
        new_post.author = user # 모델에 사용자 저장 하기 위해 불러옴/venv
        new_post.content = request.POST.get('content','') #모델에 글 저장하기
        new_image.image = request.POST.get('image', '') 
        print(request.POST)
        new_post.save()
        new_image.save()
        # redirect도 네이밍 이용해서 넘겨주셍요
        return redirect('instapost:index') # elif가 실행되지 않으면 'index'로 되돌아감


# 221003 최해민 댓글기능을 위해 임시로 render 생성
def post(request):
    return render(request, 'post.html')
def detail_page(request):
    return render(request, 'detail-page.html')

