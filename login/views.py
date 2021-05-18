import csv
import time
import traceback

from django.contrib import messages
from django.db import connection, transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models as md
from django.views.decorators.clickjacking import xframe_options_exempt
from . import models, forms
import hashlib
import xlrd
import xlwt
from datetime import datetime


# Create your views here.
class Variable(md.Model):
    Variable_name = md.CharField(max_length=128, primary_key=True)
    Value = md.IntegerField()

    def __str__(self):
        return self.Variable_name


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
    # if request.session.get('is_login', None):  # 已登录不允许重复登录
    #     return redirect('/main/')
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
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
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
                request.session['is_admin'] = True
                request.session['admin_id'] = user.id
                request.session['admin_name'] = user.name
                return redirect('/manager/')
            else:
                message = '数据库口令错误！'
                return render(request, 'login/adminlogin.html', {'message': message})
        else:
            return render(request, 'login/adminlogin.html', {'message': message})
    return render(request, 'login/adminlogin.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，不用登出
        return redirect("/login/")
    request.session.flush()
    return redirect('/login/')


def adminlogout(request):
    if not request.session.get('is_admin', None):
        # 如果本来就未登录，不用登出
        return redirect("/adminlogin/")
    request.session.flush()
    return redirect('/adminlogin/')


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


# 用户主界面
def main(request):
    if not request.session.get('is_login', None):  # 未登录，不允许直接访问
        return redirect('/login/')
    return render(request, 'login/main.html', locals())


def manager(request):
    if not request.session.get('is_admin', None):  # 未登录，不允许直接访问
        return redirect('/adminlogin/')
    return render(request, 'login/manager.html', locals())


def datamanage(request):
    if not request.session.get('is_admin', None) and not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/datamanage.html', locals())


def importdata(request):
    # TODO 导入进度条
    once_row = 100  # 每次读取行数，可修改
    earfcn_list = [37900, 38098, 38400, 38496, 38544, 38950, 39148]
    pci_list = [x for x in range(504)]
    vendor_list = ['华为', '中兴', '诺西', '爱立信', '贝尔', '大唐']
    style_list = ['室分', '宏站']
    if not request.session.get('is_admin', None) and not request.session.get('is_login', None):
        return redirect('/login/')
    if request.method == 'POST':
        f = request.FILES['upfile']
        filetype = f.name.split('.')[2]
        if filetype == 'xlsx' or filetype == 'xls':
            wb = xlrd.open_workbook(filename=None, file_contents=f.read())  # 打开表对象
            table = wb.sheets()[0]  # 获取sheet1
            nrows = table.nrows  # 总行数
            message = '导入成功！'
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
                                    row[12]) <= 90.00000 and row[13] in style_list and not isinstance(row[18], str) \
                                        and row[18] == row[16] + row[17]:
                                    # if models.Tbcell.objects.filter(sector_id=row[1]):
                                    #     # 数据已存在，先删除原数据
                                    #     models.Tbcell.objects.filter(sector_id=row[1]).delete()
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
                    message = '导入有误！请查看日志文件'
                    # 尚需加入logging模块
            elif request.POST['table'] == 'tbkpi':
                try:
                    with transaction.atomic():
                        cur_row = 1
                        while cur_row < nrows:
                            cnt = 0
                            row_list = []
                            while cnt < once_row and cur_row < nrows:
                                row = table.row_values(cur_row)
                                # 解决主键重复问题，多字段主键
                                if row[0] != '' and row[2] != '' and row[3] != '':
                                    date_pre = time.strptime(row[0], "%m/%d/%Y %H:%M:%S")
                                    line = models.Tbkpi(date=time.strftime("%Y-%m-%d %H:%M:%S", date_pre),
                                                        # 读入是str，日期格式转换
                                                        enodeb_name=row[1],
                                                        sector=row[2],
                                                        sector_name=row[3],
                                                        rpc_establish=int(row[4]),
                                                        rpc_request=int(row[5]),
                                                        rpc_succrate=None if row[5] == 0 or isinstance(row[5],
                                                                                                       str) or isinstance(
                                                            row[6], str) else float(row[4]) / float(row[5]),
                                                        erab_succ=int(row[7]),
                                                        erab_att=int(row[8]),
                                                        erab_succrate=float(row[9]),
                                                        enodeb_erab_ex=int(row[10]),
                                                        sector_switch_erab_ex=int(row[11]),
                                                        erab_lossrate=float(row[12]),
                                                        ay=float(row[13]),
                                                        enodeb_reset_ue_release=int(row[14]),
                                                        ue_ex_release=int(row[15]),
                                                        ue_succ=int(row[16]),
                                                        lossrate=float(row[17]),
                                                        enodeb_in_diff_succ=int(row[18]),
                                                        enodeb_in_diff_att=int(row[19]),
                                                        enodeb_in_same_succ=int(row[20]),
                                                        enodeb_in_same_att=int(row[21]),
                                                        enodeb_out_diff_succ=int(row[22]),
                                                        enodeb_out_diff_att=int(row[23]),
                                                        enodeb_out_same_succ=int(row[24]),
                                                        enodeb_out_same_att=int(row[25]),
                                                        enodeb_in_succrate=float(row[26]) if not isinstance(row[26],
                                                                                                            str) else None,
                                                        enodeb_out_succrate=float(row[27]) if not isinstance(row[27],
                                                                                                             str) else None,
                                                        enodeb_same_succrate=float(row[28]) if not isinstance(row[28],
                                                                                                              str) else None,
                                                        enodeb_diff_succrate=float(row[29]) if not isinstance(row[29],
                                                                                                              str) else None,
                                                        enodeb_switch_succrate=float(row[30]) if not isinstance(row[30],
                                                                                                                str) else None,
                                                        pdcp_up=int(row[31]),
                                                        pdcp_down=int(row[32]),
                                                        rpc_rebuild=int(row[33]),
                                                        rpc_rebuildrate=float(row[34]),
                                                        rebuild_enodeb_out_same_succ=int(row[35]),
                                                        rebuild_enodeb_out_diff_succ=int(row[36]),
                                                        rebuild_enodeb_in_same_succ=int(row[37]),
                                                        rebuild_enodeb_in_diff_succ=int(row[38]),
                                                        enb_in_succ=int(row[39]),
                                                        eno_in_request=int(row[40]))
                                    row_list.append(line)
                                else:
                                    pass
                                cnt += 1
                                cur_row += 1
                            models.Tbkpi.objects.bulk_create(row_list)
                except Exception as e:
                    print(e.args)
                    message = '导入有误！请查看日志文件'
            #         TODO  大表不要一次性读入内存磁盘
            elif request.POST['table'] == 'tbprb':
                try:
                    once_row = 1000
                    with transaction.atomic():
                        cur_row = 1
                        while cur_row < nrows:
                            cnt = 0
                            row_list = []
                            while cnt < once_row and cur_row < nrows:
                                row = table.row_values(cur_row)
                                date_pre = time.strptime(row[0], "%m/%d/%Y %H:%M:%S")
                                if row[0] != '' and row[3] != '':
                                    line = models.Tbprb(time.strftime("%Y-%m-%d %H:%M:%S", date_pre),
                                                        enodeb_name=row[1],
                                                        sector_description=row[2],
                                                        sector_name=row[3],
                                                        avr_noise_prb0=int(row[4]),
                                                        avr_noise_prb1=int(row[5]),
                                                        avr_noise_prb2=int(row[6]),
                                                        avr_noise_prb3=int(row[7]),
                                                        avr_noise_prb4=int(row[8]),
                                                        avr_noise_prb5=int(row[9]),
                                                        avr_noise_prb6=int(row[10]),
                                                        avr_noise_prb7=int(row[11]),
                                                        avr_noise_prb8=int(row[12]),
                                                        avr_noise_prb9=int(row[13]),
                                                        avr_noise_prb10=int(row[14]),
                                                        avr_noise_prb11=int(row[15]),
                                                        avr_noise_prb12=int(row[16]),
                                                        avr_noise_prb13=int(row[17]),
                                                        avr_noise_prb14=int(row[18]),
                                                        avr_noise_prb15=int(row[19]),
                                                        avr_noise_prb16=int(row[20]),
                                                        avr_noise_prb17=int(row[21]),
                                                        avr_noise_prb18=int(row[22]),
                                                        avr_noise_prb19=int(row[23]),
                                                        avr_noise_prb20=int(row[24]),
                                                        avr_noise_prb21=int(row[25]),
                                                        avr_noise_prb22=int(row[26]),
                                                        avr_noise_prb23=int(row[27]),
                                                        avr_noise_prb24=int(row[28]),
                                                        avr_noise_prb25=int(row[29]),
                                                        avr_noise_prb26=int(row[30]),
                                                        avr_noise_prb27=int(row[31]),
                                                        avr_noise_prb28=int(row[32]),
                                                        avr_noise_prb29=int(row[33]),
                                                        avr_noise_prb30=int(row[34]),
                                                        avr_noise_prb31=int(row[35]),
                                                        avr_noise_prb32=int(row[36]),
                                                        avr_noise_prb33=int(row[37]),
                                                        avr_noise_prb34=int(row[38]),
                                                        avr_noise_prb35=int(row[39]),
                                                        avr_noise_prb36=int(row[40]),
                                                        avr_noise_prb37=int(row[41]),
                                                        avr_noise_prb38=int(row[42]),
                                                        avr_noise_prb39=int(row[43]),
                                                        avr_noise_prb40=int(row[44]),
                                                        avr_noise_prb41=int(row[45]),
                                                        avr_noise_prb42=int(row[46]),
                                                        avr_noise_prb43=int(row[47]),
                                                        avr_noise_prb44=int(row[48]),
                                                        avr_noise_prb45=int(row[49]),
                                                        avr_noise_prb46=int(row[50]),
                                                        avr_noise_prb47=int(row[51]),
                                                        avr_noise_prb48=int(row[52]),
                                                        avr_noise_prb49=int(row[53]),
                                                        avr_noise_prb50=int(row[54]),
                                                        avr_noise_prb51=int(row[55]),
                                                        avr_noise_prb52=int(row[56]),
                                                        avr_noise_prb53=int(row[57]),
                                                        avr_noise_prb54=int(row[58]),
                                                        avr_noise_prb55=int(row[59]),
                                                        avr_noise_prb56=int(row[60]),
                                                        avr_noise_prb57=int(row[61]),
                                                        avr_noise_prb58=int(row[62]),
                                                        avr_noise_prb59=int(row[63]),
                                                        avr_noise_prb60=int(row[64]),
                                                        avr_noise_prb61=int(row[65]),
                                                        avr_noise_prb62=int(row[66]),
                                                        avr_noise_prb63=int(row[67]),
                                                        avr_noise_prb64=int(row[68]),
                                                        avr_noise_prb65=int(row[69]),
                                                        avr_noise_prb66=int(row[70]),
                                                        avr_noise_prb67=int(row[71]),
                                                        avr_noise_prb68=int(row[72]),
                                                        avr_noise_prb69=int(row[73]),
                                                        avr_noise_prb70=int(row[74]),
                                                        avr_noise_prb71=int(row[75]),
                                                        avr_noise_prb72=int(row[76]),
                                                        avr_noise_prb73=int(row[77]),
                                                        avr_noise_prb74=int(row[78]),
                                                        avr_noise_prb75=int(row[79]),
                                                        avr_noise_prb76=int(row[80]),
                                                        avr_noise_prb77=int(row[81]),
                                                        avr_noise_prb78=int(row[82]),
                                                        avr_noise_prb79=int(row[83]),
                                                        avr_noise_prb80=int(row[84]),
                                                        avr_noise_prb81=int(row[85]),
                                                        avr_noise_prb82=int(row[86]),
                                                        avr_noise_prb83=int(row[87]),
                                                        avr_noise_prb84=int(row[88]),
                                                        avr_noise_prb85=int(row[89]),
                                                        avr_noise_prb86=int(row[90]),
                                                        avr_noise_prb87=int(row[91]),
                                                        avr_noise_prb88=int(row[92]),
                                                        avr_noise_prb89=int(row[93]),
                                                        avr_noise_prb90=int(row[94]),
                                                        avr_noise_prb91=int(row[95]),
                                                        avr_noise_prb92=int(row[96]),
                                                        avr_noise_prb93=int(row[97]),
                                                        avr_noise_prb94=int(row[98]),
                                                        avr_noise_prb95=int(row[99]),
                                                        avr_noise_prb96=int(row[100]),
                                                        avr_noise_prb97=int(row[101]),
                                                        avr_noise_prb98=int(row[102]),
                                                        avr_noise_prb99=int(row[103]))
                                    row_list.append(line)
                                else:
                                    pass
                                cnt += 1
                                cur_row += 1
                            models.Tbprb.objects.bulk_create(row_list)
                except Exception as e:
                    print(e.args)
                    message = '导入有误！请查看日志文件'
            elif request.POST['table'] == 'tbmrodata':
                try:
                    with transaction.atomic():
                        cur_row = 1
                        while cur_row < nrows:
                            cnt = 0
                            row_list = []
                            while cnt < once_row and cur_row < nrows:
                                row = table.row_values(cur_row)
                                if True:
                                    line = models.Tbmrodata(TimeStamp=row[0],
                                                            ServingSector=row[1],
                                                            InterferingSector=row[2],
                                                            LteScRSRP=float(row[3]),
                                                            LteNcRSRP=float(row[4]),
                                                            LteNcEarfcn=int(row[5]),
                                                            LteNcPci=int(row[6]))
                                    row_list.append(line)
                                else:
                                    pass
                                cnt += 1
                                cur_row += 1
                            models.Tbmrodata.objects.bulk_create(row_list)
                except Exception as e:
                    print(e.args)
                    message = '导入有误！请查看日志文件'
        elif filetype == 'csv':
            pass
        # TODO 跳转地址需要回到父目录
        return render(request, 'login/datamanage.html', {'message': message})
    return render(request, 'login/datamanage.html')


def exportdata(request):
    if not request.session.get('is_admin', None) and not request.session.get('is_login', None):
        return redirect('/login/')
    if request.method == 'POST':
        table_name = request.POST['tables-export']
        format = request.POST['format']
        if format == 'excel':
            response = HttpResponse(content_type='application/ms-excel')
        else:
            response = HttpResponse(content_type='text/csv')
        if (table_name == 'tbCell'):
            rows = models.Tbcell.objects.all()
        elif (table_name == 'tbKPI'):
            rows = models.Tbkpi.objects.all()
        elif (table_name == 'tbPRB'):
            rows = models.Tbprb.objects.all()
        else:
            rows = models.Tbmrodata.objects.all()
        rows_list = list(rows.values())
        columns = []
        if not rows:
            return render(request, "login/datamanage.html", {'message': '此数据表为空！'})
        for key in rows_list[0]:
            columns.append(key)
        try:
            if format == 'excel':
                # response = HttpResponse(content_type='application/ms-excel')
                response['Content-Disposition'] = 'attachment; filename="' + table_name + '.xls"'
                wb = xlwt.Workbook(encoding='utf-8')
                ws = wb.add_sheet(table_name)
                # Sheet header, first row
                row_num = 0
                font_style = xlwt.XFStyle()
                font_style.font.bold = True
                # Sheet body, remaining rows
                font_style = xlwt.XFStyle()
                for col_num in range(len(columns)):
                    ws.write(row_num, col_num, columns[col_num], font_style)
                for row in rows_list:
                    row_num += 1
                    # print(row.get(columns[0]))
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, row.get(columns[col_num]), font_style)
                wb.save(response)
                return response
            else:
                # response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="' + table_name + '.csv"'
                writer = csv.writer(response)
                writer.writerow(columns)
                for row in rows_list:
                    writer.writerow(row.values())
                return response
        except:
            print('error')
    return response


# TODO 之后增加下拉框，用户能自由选择修改哪个缓冲区
def connectmanage(request):
    if request.method == "POST":
        time = request.POST.get('time')
        cachesize = request.POST.get('cachesize')
        if time != "":
            sql = "set global wait_timeout=" + time + ';'
            cursor = connection.cursor()
            try:
                cursor.execute(sql)
                transaction.commit()
                messages.success(request, "修改成功！")
            except Exception as e:
                traceback.print_exc(e)
        if cachesize != "":
            sql = "set  global key_buffer_size=" + cachesize + ';'
            cursor = connection.cursor()
            try:
                cursor.execute(sql)
                transaction.commit()
                messages.success(request, "修改成功！")
            except Exception as e:
                traceback.print_exc(e)
    return render(request, 'login/conmanage.html', locals())


# 允许该页面在<frame>中展示
@xframe_options_exempt
def initframe(request):
    return render(request, 'login/frame.html', locals())


@xframe_options_exempt
def infocate1(request):
    for var in Variable.objects.raw("show global variables like 'wait_timeout';"):
        wait_timeout = var.Value
    for variable in Variable.objects.raw("show global variables like 'interactive_timeout';"):
        interactive_timeout = variable.Value
    return render(request, 'login/info/cate1.html', locals())


@xframe_options_exempt
def infocate2(request):
    var_map = {}
    for var in Variable.objects.raw('show global variables;'):
        var_map[var.Variable_name] = var.Value
    print(var_map)
    return render(request, 'login/info/cate2.html', locals())


@xframe_options_exempt
def infocate3(request):
    for var in Variable.objects.raw("show global variables like 'key_buffer_size';"):
        key_buffer_size = var.Value
    return render(request, 'login/info/cate3.html', locals())


'''业务查询功能'''


def info_query(request):
    return render(request, 'login/query/info_query.html', locals())


# show information of cell settings
def cell_info(request):
    if request.method == "POST":
        pass
    # TODO 过滤出所有小区名，并传递给前端
    return render(request, 'login/query/cell_info.html', locals())


def enodeb_info(request):
    if request.method == "POST":
        pass
    return render(request, 'login/query/enodeb_info.html', locals())


def kpi_info(request):
    if request.method == "POST":
        pass
    return render(request, 'login/query/kpi_info.html', locals())


def prb_info(request):
    if request.method == "POST":
        pass
    return render(request, 'login/query/prb_info.html', locals())
