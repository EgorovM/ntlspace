# coding=utf-8

from django.http                    import HttpResponse, HttpResponseRedirect
from django.shortcuts               import render, get_object_or_404
from django.contrib                 import auth
from django.contrib.auth.decorators import login_required
from django.core.mail               import send_mass_mail
from django.db                      import IntegrityError

from teacher.models import *
from teacher.forms  import *


### request handlers

def register(request):
    profile_form = TeacherProfileForm()
    user_form = UserForm()

    return render(request, 'teacher/register.html', locals())
