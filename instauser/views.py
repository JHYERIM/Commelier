from django.shortcuts import render, redirect
from instauser.models import InstaUser
# Create your views here.

# 220930 최해민 회원가입후 로그인페이지로 보내기 위한 함수
def login(request):
    return render(request, 'login.html')

# 220930 최해민 회원가입 기능 함수
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email') # 중복검사
        # 이메일이 맞는지 확인
        # 
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        is_dating = request.POST.get('is_dating')
        
        instauser = InstaUser(email = email, 
                              name = name, 
                              nickname = nickname, 
                              password = password,
                              is_dating = is_dating,)
        instauser.save()
        return redirect('instauser:login')
    
    if request.method == 'GET':
        return render(request, 'signup.html')
    