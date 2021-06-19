from django.shortcuts import redirect, render
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    request.session['send']= "register"
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        request.session['alias']= request.POST['alias']
        pw_hash= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        user= User.objects.create(name= request.POST['name'], alias=request.POST['alias'], birthday= request.POST['birthday'], email= request.POST['email'], password= pw_hash)
        request.session['user_id'] = user.id
        request.session['send'] = "registered"
        return redirect('/books')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        request.session['send']= "login"
        if errors:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')
        else:
            log_user= User.objects.filter(email=request.POST['email'])
            if len(log_user) != 1:
                return redirect('/')
            if log_user:
                user= log_user[0]
                request.session['alias'] = user.alias
                if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                    request.session['user_id']= user.id
                    print(request.POST)
                    request.session['send'] = "logged in"
                    return redirect('/books')
    else:
        return redirect('/')

def success(request):
    return render(request, 'success.html')

def logout(request):
    request.session.clear()
    return redirect('/')
