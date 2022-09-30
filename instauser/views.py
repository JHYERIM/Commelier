from django.shortcuts import render , redirect
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