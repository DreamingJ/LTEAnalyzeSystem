# LTEAnalyzeSystem
A web project devloped by Django+Mysql
## 准备
Clone后，使用Pycharm打开本项目
### 环境配置：
- Run configurations 选择DJango server
- Settings>Languages&Frameworks>Django
    - project root设置为当前项目目录
    - settings设置为LTEsystem\settings.py
    - Manage Script设置为manage.py
### 数据库配置：
连接：  

LTEsystem\settings.py文件设置DATABASES  

使ORM生效，需执行命令:
```
python manage.py makemigrations  
python manage.py migrate  
```
注意：  
Models.py中的模型类字段要和Mysql数据库表对应
