from django.shortcuts import render,redirect
from df_user import models
from hashlib import sha1

# Create your views here.
def login(request):
    return render(request,'df_user/login.html')
def register(request):
    return render(request,'df_user/register.html')
def register_handle(request):
    print('231321')
    post = request.POST

    name = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')

    if pwd != cpwd:
        return redirect('/user/register/')

    s1=sha1()
    s1.update(pwd.encode("utf8"))
    pwd2 = s1.hexdigest()


    #创建对象，存入数据库
    user = models.UserInfo()
    user.uname = name
    user.upwd = pwd2
    user.uemail = email
    user.save()
    return redirect('/user/login/')