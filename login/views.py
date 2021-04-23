from django.shortcuts import render, redirect
from . import models, forms
import hashlib


# Create your views here.


# To encode the password
def hash_code(s, salt='LTEsystem'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def hello(request):
    return render(request, 'login/index.html')


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请重新检查填写内容！'
        if username.strip() and password:  # 确保用户名和密码都不为空
            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在！'
                return render(request, 'login/login.html', {'message': message})
            # 使用密码哈希值进行比对
            if user.password == hash_code(password):
                return redirect('/main/')
            else:
                message = '密码错误！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')


def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        dbpassword = request.POST.get('dbpassword')
        message = '请重新检查填写内容！'
        if username.strip() and password and dbpassword:
            try:
                user = models.Admin.objects.get(name=username)
            except:
                message = '该帐户不存在！'
                return render(request, 'login/adminlogin.html', {'message': message})

            if user.password != password:
                message = '密码错误！'
                return render(request, 'login/adminlogin.html', {'message': message})
            elif user.dbpassword == dbpassword:
                return redirect('/manager/')
            else:
                message = '数据库口令错误！'
                return render(request, 'login/adminlogin.html', {'message': message})
        else:
            return render(request, 'login/adminlogin.html', {'message': message})
    return render(request, 'login/adminlogin.html')


def register(request):
    """实现注册功能，首先检查两次密码是否相同，再检查用户名是否已存在"""
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


# 用户登出
def logout(request):
    return redirect('/login/')


# 用户主界面
def main(request):
    return render(request, 'login/main.html', locals())


def manager(request):
    return render(request, 'login/manager.html', locals())
