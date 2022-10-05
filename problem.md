# 트러블 슈팅
<br>

## ⚠️ 문제 해결

<br>

---

<br>
<h3>🔒 비밀번호 검증 오류</h3>
<br>

- 아이디를 생성하고 로그인을 시도했으나,정상적으로 로그인이 진행되지 않았습니다.
- 해당 문제는 비밀번호가 데이터베이스에 저장되는 과정에서 암호화 되지 않고 저장되면서, 로그인 검증을 통과하지 못하면서 발생했습니다.
- 이를 해결하기 위해 다음과 같은 코드를 추가하여 데이터베이스에 저장되는 비밀번호를 암호화 했습니다.

<br>

```python
                    instauser = InstaUser(username = username,
                                        nickname = nickname,
                                        is_dating = is_dating,)
                    
                    # set_password() 함수는 Django 유저 비밀번호를 암호화해주는 함수입니다. 이를 추가해 비밀번호가 평문으로 저장되는 것을 방지합니다. 
                    instauser.set_password(password) 
                    instauser.save()
                    
                    return redirect('instauser:login')
```

<br>

---

<br><br>
<h3> 📄 게시글 이미지, 데이터베이스와 상호작용 오류</h3>
<br>

POST로 이미지 보내는 것을 시도했으나, 이미지를 받을 수 없었고, 데이터베이스에도 저장이 되지 않는 에러가 발생했습니다.

<br>

```python
        def create_post(request):
            if request.method == 'GET':
                user = request.user.is_authenticated  
                if user: 
                    return render(request, 'new_post.html')
                else:  
                    return redirect('/login/')
            
            elif request.method == 'POST': 
                new_post = Instapost( ) 
                new_image = Image( ) 
                new_post.author = user 
                new_post.content = request.POST.get('content','')
                new_post.save()
                #1. 경로 지정 설정 문제.
                #request.FILES.get('','') Html의 name의 용도를 정확하게 이해하지 않고 사용하면서 문제가 발생했다. 
                new_image.image = request.FILES.get('images', '')
                new_image.instapost = new_post
                new_image.save()
               
                return redirect('instapost:index')

                
```

<br>
1. 경로 지정 설정 문제.


- 프론트에서 백엔드로 데이터를 가져오는 코드를 작성하면서, 'Html'의 'name'의 용도를 정확하게 알지 못하고, 전혀 다른 입력값을 입력하면서 데이터를 입력 받지 못하는 문제가 발생했다. 
- 이를 해결하기 위해서 헷갈리는 'name' 들을 정리하는 과정을 거쳤다.

<br>
2. 이미지를 저장을 못했었다.
 
 
  - Image 모델의 객체를 new_image라고 선언해주고, 이미지 파일을 저장할 때 저장하지 못하는 에러가 있었습니다.

<br>

```python
# models.py
class Image(models.Model):
    image = models.ImageField(blank =True ,null=True ,upload_to='images') 
    instapost = models.ForeignKey(Instapost, on_delete=models.CASCADE, related_name='images')
```

- Image 모델은 Instapost라는 모델을 외래키로 받아오고 있었고, 우리는 Instapost 모델의 객체만 생성한 채 속성에 저장해주고 있었습니다.

- 해결방법으로 먼저 new_post라는 Instapost의 객체를 먼저 저장해주고나서 new_image라는 Image모델 객체의 속성 instapost에 저장해 주었습니다.

<br>

---

<br><br>

### 📄 게시글 수정시, PK값 불일치로 인한 오류
- 게시글 수정 시 게시글의 pk값과 이미지의 pk값이 같지 않아, 게시물만 수정이 되고, 이미지 수정 값이 무시되고 게시글이 삭제 되지 않는 에러가 발생했습니다.
<br><br>

```python
#models.py
instapost = models.ForeignKey(Instapost, on_delete=models.CASCADE,)
```
```python
#views.py
def remove_post(request, pk):
    post = Instapost.objects.get(pk=pk) 
    # image = Image.objects.get(pk=pk)
    if request.method =='POST':           
        post.delete()
        # image.delete()                   
        return redirect('instapost:index')
    return render(request, 'detali-page_1.html', {'Instapost:post'})
```

<br>

- 게시글의 pk값에 이미지값을 참조시켜 게시글을 삭제하면 자동으로 이미지까지 삭제 되기 때문에
생성했던 이미지 클래스와 delete함수를 삭제함으로서 오류를 해결했습니다.
<br><br>

----

<br><br>

### ↩ 역참조
- 한 게시글의 여러 댓글들을 가져올 때, View의 함수에서 받아오는 id값이 게시글의 id만 받아오게 함수를 작성했었습니다.
- 댓글 객체들을 Django ORM을 통해 DB에서 조회해올 때 작성하기 어려운 문제가 있었습니다.

해당 부분을 ForeinKey를 이용해 역참조해서 간편하게 받아올 수 있었습니다.

> 역참조 : ForeinKey에 의해 참조되고 있는 모델에서 참조하는 모델을 호출하는 경우를 **역참조**라고 한다.

```python
class InstaComment(models.Model):
    (중략)
    instapost = models.ForeignKey(Instapost, on_delete=models.CASCADE, related_name='comments')
```

위와 같이 모델 선언시 속성값에 related_name을 인자로 넘겨주어 간편하게 역참조할 수 있습니다.

Django Template Language를 사용해 템플릿에서 역참조도 가능합니다.

```django html
{% for comment in instapost.comments.all %}
    ...
    (중략)
    ...
    {{ comment.author.nickname }}
    {{ comment.content }}
{% endfor %}
```

위와 같이 작성하여, 이해하기 쉽고 작성하기 편하게 댓글기능을 구현했습니다.

