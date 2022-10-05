from django.shortcuts import render , redirect
from instauser.models import InstaUser

# 221002 최해민 유저생성 검증을 위한 함수 import
from django.contrib.auth import get_user_model # 사용자가 DB안에 있는지 검사하는 함수.
from django.contrib.auth import  authenticate,login ,logout


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user=user)
            return redirect('instauser:profile')
        else:
            return redirect('instauser:login')

    if request.user.is_authenticated:
        return redirect('instauser:profile')
    else:
        return redirect('instauser:login')
      

#'%s?next=%s' : 기본적으로 인증 성공시 사용자를 리다이렉트하는 경로는 "next"라는 쿼리 문자열 매개 변수에  저장

def logout_view(request):
    logout(request)
    return redirect('instauser:login')


def profile_view(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            instauser = InstaUser.objects.get(id=request.user.id)
            instaposts = instauser.instaposts.all()
            
            return render(request,'profile.html', {'instauser':instauser, 'instaposts':instaposts})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/login/')

    

# 220930 최해민 회원가입후 로그인페이지로 보내기 위한 함수
# def login(request):
#     return render(request, 'login.html')

# 220930 최해민 회원가입 기능 함수
def signup(request):
    # 221003 최해민 이미 로그인한 회원이면, 프로필 페이지로 넘겨준다.
    if request.user.is_authenticated:
        return redirect('instauser:profile')
    
    # 221003 최해민 이미 로그인한 회원이 아니면 다음을 실행한다.
    else:
        if request.method == 'GET':
            return render(request, 'signup.html')
        
        if request.method == 'POST':
            username = request.POST.get('username')
            nickname = request.POST.get('nickname')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            is_dating = request.POST.get('is_dating')
            
            # 221002 최해민 password가 올바른지 확인하는 분기문
            if password != password2: # password와 password2가 같지 않다면
                return render(request, 'signup.html', {'error' : '비밀번호를 확인해 주십시오.'}) # error를 넘겨주어 알람을 보여준다.
            
            else: # password 확인이 맞을때
                if username == "" or password == "": # 이메일과 패스워드가 공란일 때
                    return render(request, 'signup.html', {'error' : 'ID 또는 비밀번호를 입력 안하셨습니다.'})
                
                # 221002 최해민 이미 존재하는 유저가 있는지 확인하기 위한 변수 선언(True, False로 반환)
                exist_user = get_user_model().objects.filter(username = username)
                
                if exist_user: # 이미 존재하는 유저가 있을 때
                    return render(request, 'signup.html', {'error' : '동일한 ID가 존재합니다.'})
                
                else:
                    instauser = InstaUser(username = username,
                                        nickname = nickname,
                                        is_dating = is_dating,)
                    
                    instauser.set_password(password)
                    instauser.save()
                    
                    return redirect('instauser:login')


