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


### helpers

def login(request, login, password):
    user = auth.authenticate(username = login, password = password)
    if user != None and user.is_active:
        auth.login(request, user)

        return user

    return None

### request handlers

def index(request):
    has_error     = False
    error_message = ""

    authorized = request.user.is_authenticated()

    if authorized:
        return HttpResponseRedirect("/" + request.user.profile.username + "/")

    if request.method == "POST" and "sign_in" in request.POST:
        login    = request.POST['login']
        password = request.POST['password']

        user = login(request, login, password)
        if user:
            return HttpResponseRedirect("/" + request.user.profile.username + "/")
        else:
            has_error     = True
            error_message = "Не удалось войти в систему"

    return render(request, 'main/index.html', locals())
