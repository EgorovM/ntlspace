#coding=utf-8
from django.shortcuts           import render, HttpResponseRedirect, redirect
from django.utils               import timezone
from django.db                  import IntegrityError
from django.core.paginator      import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth        import authenticate
from django.contrib             import auth
from PIL                        import Image

from .models    import *
from .forms     import *
from main.views import sign_in, redirect_to_profile

 
def register(request):
    error_message = ""
    user_form    = UserForm()
    profile_form = StudentProfileForm()
    
    if request.method == "POST":
        user_form    = UserForm(request.POST)
        profile_form = StudentProfileForm(request.POST,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user    = user_form.save()
            profile = profile_form.save(commit = False)

            profile.user = user
            profile.save()

            username = user_form["username"].value()
            password = user_form["password"].value()

            user = sign_in(request, username, password)

            if user:
                return redirect_to_profile(user)
       
    return render(request,'student/register.html',locals())
    
def profile(request, nick):
    context = []
    
    if request.method == "POST":
        pass
        
    user       = request.user
    authorized = request.user.is_authenticated()
    
    if authorized:
        profile = StudentProfile.objects.get(user=user)      
    
    return render(request, 'student/profile.html', locals())
    
