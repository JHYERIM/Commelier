# 221003 최해민 import redirect 추가
from django.shortcuts import render, redirect
from .models import Instapost, Image, InstaComment


# Create your views here.
def index(request):
    # 221004 최해민, 박소민 post_list 최신순으로 정렬 후 값 넘겨주기
    post_list = Instapost.objects.all().order_by('-id')
    return render(request, 'index.html', {'post_list' : post_list})


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
        new_image.image = request.FILES.get('images', '') 
        print(request.POST)
        new_post.save()
        new_image.save()
        # redirect도 네이밍 이용해서 넘겨주셍요
        return redirect('instapost:index') # elif가 실행되지 않으면 'index'로 되돌아감


# 221004 최신욱 문규빈 장혜림 게시물 수정 및 삭제 기능 추가.

# 게시글 수정하기 눌렀을 때. <페이지 이동>

def edit(request, pk):
    instapost = Instapost.objects.get(pk=pk)             # 인스타포스트안에 있는 값들을 전부 다 불러옴.
    context = {                                          # 인스타포스트 내용 값.   
        'instapost': instapost,
    }
    return render(request, 'post_edit.html', context) 

# 게시글 수정하기를 눌렀을 때, 업데이트. <적용>

def update(request, pk):
     instapost = Instapost.objects.get(pk=pk) #게시글 데이터를 instapost에 담아준다.
     image = Image.objects.get(pk=pk)       # 게시글 이미지 데이터를 불러와서 image에 담아줌

     # 게시글 변경사항 저장 하기. 
    
     if request.method == 'POST': #수정요청이 왔을 때 덮어쓰기
        instapost.content = request.POST.get('content')
        image.image= request.FILES.get('images')
        instapost.save()
        image.save()
        return redirect(str(instapost.pk), 'instapost:index') 
     
     # 게시글 수정사항 입력 페이지에 처음 접속했을 때.       

     else:
        return redirect('detail-page_1') # 게시글 수정을 눌렀을 때, 기존 데이터가 수정하기 페이지에 저장된 상태로 나타나짐


# 게시글 삭제 기능.
def remove_post(request, pk):
    post = Instapost.objects.get(pk=pk) # 데이터를 불러와서 post 저장함.
    image = Image.objects.get(pk=pk)
    if request.method =='POST':           
        post.delete()
        image.delete()                     #데이터를 삭제합니다.
        return redirect('instapost:index')
    return render(request, 'detali-page_1.html', {'Instapost:post'})




# 221003 최해민 댓글기능을 위해 임시로 render 생성
def detail_post(request, id):
    # 1번 게시물을 가져왔음.
    instapost = Instapost.objects.get(id=id)
    # 1번 게시물에 달린 댓글들을 모두 가져와야 함
    comments = InstaComment.objects.filter(instapost_id = id)
    return render(request, 'detail-page.html', {'instapost' : instapost, 
                                                'comments': comments, 
                                                })
# comments = [댓글1, 댓글2, 댓글3, 댓글4 ...]

# 221004 박소민, 최해민 댓글생성 함수 추가
def create_comment(request, id):
    # 이 request가 POST인지 확인
    if request.method == 'POST':
        # POST방식으로 넘어온 content 데이터가 있습니다. 데이터를 변수에 담아주세요.
        content = request.POST.get('content','')
        # 만약에 POST가 맞다면, 붕어빵을 하나 만들어주세요
        instacomment = InstaComment()
        # 붕어빵의 content에 데이터 변수를 넣어주세요
        instacomment.content = content
        instacomment.author = request.user
        # 어느 게시물에 달린 댓글인지 구분이 필요
        # 어느 게시물인지 부터 정해줘야하는데, 그걸 함수의 인자(id)
        # Instapost.objects 라는 붕어빵들 중에서 id를 대조해서 하나 가져옵니다.
        instacomment.instapost = Instapost.objects.get(id=id)
        # 마지막으로 저장 해주시면 됩니다.
        instacomment.save()
        
        # 저장이 끝났으면, detail_post로 보내주세요.
    return redirect('/instapost/'+str(id))
# 127.0.0.1:8000/instapost/<int:id>


# 221004 최해민 댓글 삭제 함수 추가
def delete_comment(request, id):
    # html에서 넘겨준 comment.id를 이용하여 댓글 객체를 가져온다.
    comment = InstaComment.objects.get(id = id)
    # 삭제한 후 다시 상세페이지를 띄워주기 위해 변수에 저장해 둔다
    now_instapost = comment.instapost.id
    comment.delete()
    return redirect('/instapost/'+str(now_instapost))
