from django.shortcuts import render ,redirect
from .models import Posting #



# Create your views here.
def index(request):
    return render(request, 'index.html')

# 220930 박소민, 문규빈, 장혜림 포스트생성 함수 추가가
def create_post(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            return render(request, 'index.html')
        else:  # 로그인이 되어 있지 않다면
            return redirect('login.html')
    
    elif request.method == 'POST': #요청하는 방식이 POST 방식인지 확인
        user = request.instauser #현재 로그인 한 사용자를 불러오기
        print(user)
        new_post = Posting( ) #글쓰기 모델 가져오기
        new_post.author = user # 모델에 사용자 저장 하기 위해 불러옴
        new_post.content = request.POST.get('content','') #모델에 글 저장하기
        new_post.save()
        return redirect(request, 'instapost:index') # elif가 실행되지 않으면 'create_post'로 되돌아감
    # 