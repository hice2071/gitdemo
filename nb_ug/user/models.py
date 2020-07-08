from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)         # 序号
    account = models.CharField(max_length=10)       # 账号
    password = models.CharField(max_length=10)      # 密码
    full_name = models.CharField(max_length=10)     # 姓名
    department = models.CharField(max_length=30, null=True)        # 所属部门
    position = models.CharField(max_length=10, null=True)      # 职位
    jurisdiction = models.CharField(max_length=10, null=True)      # 权限
    entry_date = models.CharField(max_length=10, null=True)        # 入职日期
    create_time = models.DateTimeField(auto_now_add=True, null=True)        # 添加时间
    visits = models.CharField(max_length=10, null=True)        # 访问次数
    finally_log_ip = models.CharField(max_length=10, null=True)        # 最后登陆ip
    finally_log_time = models.CharField(max_length=20, null=True)      # 最后登陆时间
    qq = models.CharField(max_length=20, null=True)        # qq
    mobile = models.CharField(max_length=20, null=True)        # 手机

    def __str__(self):
        return self.full_name

    # class Meta:
