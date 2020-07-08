from django.shortcuts import render
# from django.shortcuts import render.redirect

# Create your views here.
# def index(request):
#     pass
#     return render(request, 'login/index.html')
#

def login(request):
    if request.method == "POST":
        account = request.POST.get('account')
        password = request.POST.get('password')
        if account and password:  # 确保用户名和密码都不为空
            account = account.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=account)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login/login.html', {"message": message})
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


# def logout(request):
#     pass
#     return redirect('/index/')
