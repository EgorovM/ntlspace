#coding=utf-8
from .models import *
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils import timezone
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from PIL      import Image
import datetime
import json
import StringIO

def register(request):
    false_message = ""
    if request.method == "POST":
        if "register_button" in request.POST:
            username = request.POST["login"]
            password = request.POST["password"]
            full_name = request.POST["full_name"]
            sex       = request.POST["sex"]
            birthday  = request.POST["birthdate"]
            grade     = request.POST["grade"]
            letter    = request.POST["letter"]
            address   = request.POST["address"]

            if username !='' and password !='' and full_name != '' and sex != '' and birthday != '' and grade != '' and letter != '' and address != '':
                try:
                    user = User.objects.create_user(username = username, password = password)
                    user.save()
                except IntegrityError:
                    false_message = "Такой логин уже существует."
                    response = render(request, 'student/register.html',{"false_message":false_message})
                    return response

                profile           = StudentProfile(user = user)
                profile.name      = full_name
                profile.grade     = grade
                profile.letter    = letter
                profile.address   = address
                profile.sex       = sex
                profile.birthdate = birthdate
                profile.save()
                
                user = authenticate(username = username, password = password)

                if user is not None and user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect("/profile")
            else:
                false_message = "Заполните все поля."

    context = {"SEX":SEX,"GRADE":GRADE,"LETTER":LETTER,"false_message":false_message}

    return render(request,'student/register.html',context)
