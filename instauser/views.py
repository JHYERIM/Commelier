from django.shortcuts import render, redirect
from instauser.models import InstaUser
# Create your views here.

def login(request):
    return render(request, 'login.html')



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
    