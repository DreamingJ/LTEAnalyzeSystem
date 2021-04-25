from django.db import transaction
from django.shortcuts import render, redirect
from . import models, forms
import hashlib
import xlrd
import xlwt


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


def datamanage(request):
    return render(request, 'login/datamanage.html', locals())


def importdata(request):
    once_row = 50  # 每次读取行数，可修改
    earfcn_list = [37900, 38098, 38400, 38496, 38544, 38950, 39148]
    pci_list = [x for x in range(504)]
    vendor_list = ['华为', '中兴', '诺西', '爱立信', '贝尔', '大唐']
    style_list = ['室分', '宏站']
    if request.method == 'POST':
        f = request.FILES['upfile']
        filetype = f.name.split('.')[2]
        if filetype == 'xlsx' or filetype == 'xls':
            wb = xlrd.open_workbook(filename=None, file_contents=f.read())  # 打开表对象
            table = wb.sheets()[0]  # 获取sheet1
            nrows = table.nrows  # 总行数
            # 哪张目的表
            if request.POST['table'] == 'tbcell':
                try:
                    with transaction.atomic():
                        cur_row = 1  # 跳过表头，只读数据
                        while cur_row < nrows:
                            cnt = 0
                            row_list = []  # 使用行列表批量插入
                            while cnt < once_row and cur_row < nrows:
                                row = table.row_values(cur_row)  # 表的一行数据
                                # 数据清洗
                                if row[5] in earfcn_list and row[6] in pci_list and row[10] in vendor_list \
                                        and -180.00000 <= float(row[11]) <= 180.00000 and -90.00000 <= float(
                                        row[12]) <= 90.00000 and row[13] in style_list and not isinstance(row[18], str)\
                                        and row[18] == row[16] + row[17]:
                                    # 判断是否已存在该条数据
                                    line = models.Tbcell(city=row[0],
                                                         sector_id=row[1],
                                                         sector_name=row[2],
                                                         enodebid=int(row[3]),
                                                         enodeb_name=row[4],
                                                         earfcn=int(row[5]),
                                                         pci=int(row[6]),
                                                         tac=int(row[9]) if not isinstance(row[9], str) else None,
                                                         vendor=row[10],
                                                         longitude=float(row[11]),
                                                         latitude=float(row[12]),
                                                         style=row[13],
                                                         azimuth=row[14],
                                                         height=row[15] if not isinstance(row[15], str) else None,
                                                         electtilt=row[16] if not isinstance(row[9], str) else None,
                                                         mechtilt=row[17] if not isinstance(row[9], str) else None,
                                                         totletilt=row[18])
                                    row_list.append(line)

                                else:
                                    pass
                                    # 日志文件记录被剔除数据的位置、编号
                                cnt += 1
                                cur_row += 1
                            models.Tbcell.objects.bulk_create(row_list)  # 批量导入一个list
                except Exception as e:
                    print(e.args)
                    # 尚需加入logging模块
                    # return HttpResponse('出现错误...%s' % e)
            elif request.POST['table'] == 'tbkpi':
                pass
            elif request.POST['table'] == 'tbprb':
                pass
            elif request.POST['table'] == 'tbmrodata':
                pass
        elif filetype == 'csv':
            pass
        message = '导入成功！'
        return render(request, 'login/datamanage.html', {'message': message})
    return render(request, 'login/datamanage.html')


def exportdata(request):
    if request.method == 'POST':
        pass


def connectmanage(request):
    return render(request, 'login/conmanage.html', locals())