# coding=utf-8

from django.http                    import HttpResponse, HttpResponseRedirect
from django.shortcuts               import render, get_object_or_404
from django.contrib                 import auth
from django.contrib.auth.decorators import login_required
from django.core.mail               import send_mass_mail
from django.db                      import IntegrityError

from main.models    import *
from student.models import *
from teacher.models import *


TEACHER_PROFILE = 1
STUDENT_PROFILE = 2

### helpers

def sign_in(request, login, password):
    user = auth.authenticate(username = login, password = password)
    if user != None and user.is_active:
        auth.login(request, user)

        return user

    return None

def get_profile_type(user):
    if hasattr(user, "teacher_profile"):
        return TEACHER_PROFILE
    elif hasattr(user, "student_profile"):
        return STUDENT_PROFILE
    else:
        return None

def redirect_to_profile(user):
    if get_profile_type(user) == TEACHER_PROFILE:
        return HttpResponseRedirect("/teacher/" + user.username + "/")
    elif get_profile_type(user) == STUDENT_PROFILE:
        return HttpResponseRedirect("/student/" + user.username + "/")

### request handlers

def index(request):
    has_error     = False
    error_message = ""

    authorized = request.user.is_authenticated()

    if authorized:
        return redirect_to_profile(request.user)

    if request.method == "POST" and "sign_in" in request.POST:
        login    = request.POST['login']
        password = request.POST['password']

        user = sign_in(request, login, password)
        if user:
            return redirect_to_profile(request.user)
        else:
            has_error     = True
            error_message = "Не удалось войти в систему"

    return render(request, 'main/index.html', locals())
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
    
