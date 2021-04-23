from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Admin(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    dbpassword = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Meta:
    """
    元数据里定义用户按创建时间的反序排列，也就是最近的最先显示
    """
    ordering = ["-c_time"]
    verbose_name = "用户"
    verbose_name_plural = "用户"

