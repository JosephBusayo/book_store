from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User, auth
from django.contrib import messages



def register(request):
    if request.method == "POST":
        reg_form = RegisterForm(request.POST)

        if reg_form.is_valid():
            f_name = reg_form.cleaned_data["first_name"]
            l_name = reg_form.cleaned_data["last_name"]
            u_name = reg_form.cleaned_data["username"]
            mail = reg_form.cleaned_data["email"]
            pswd = reg_form.cleaned_data["password"]
            pswd2 = reg_form.cleaned_data["confirm_password"]

            if pswd != pswd2:
                print("Yes")
                #raise forms.ValidationError("wrong something")
            else:
                user = User.objects.create_user(username=u_name, password=pswd, email=mail, first_name=f_name, last_name=l_name)
                user.save()
                return redirect("/")

    reg_form = RegisterForm()
    return render(request, 'register.html', {'reg_form':reg_form})


def login(request):
    if request.method == 'POST':
        log_form = LoginForm(request.POST)

        #Note cleaned_data is only available when you use is_valid
        if log_form.is_valid():
            u_name = log_form.cleaned_data["username"]
            pswd = log_form.cleaned_data["password"]

            #check if user in database
            user = auth.authenticate(username=u_name, password=pswd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'wrong username or password')
            return redirect('login')

    log_form = LoginForm()
    return render(request, 'login.html', {'log_form':log_form})


def logout_req(request):
    auth.logout(request)
    return redirect('/')
