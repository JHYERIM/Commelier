from django.shortcuts import render , redirect
from instauser.models import InstaUser
from django.contrib.auth import authenticate ,login
from django.contrib import auth


def login_view(request):
    if request.method == "POST":
       email = request.POST['email']            #요청받은 값을 변수에 담음.
       password = request.POST['password']
                                                #들어온 아이디 비빌먼호를 검증.
       user =authenticate(email='eamil' , password='password')                                
       if user is not None:                      #이렇게 검증받은 아이디 로그인
        login(request, user)
        return redirect('')
       else:
        return render(request,'login.html'), {'error':'이메일 혹은 비밀번호를 잘못 입력하셨습니다.' }                                            


    return render(request, 'login.html')


def logout_view(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('')


# Create your views here.

# 220930 최해민 회원가입후 로그인페이지로 보내기 위한 함수
# def login(request):
#     return render(request, 'login.html')

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

