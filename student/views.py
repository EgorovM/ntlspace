#coding=utf-8
from django.shortcuts           import render, HttpResponseRedirect, redirect
from django.utils               import timezone
from django.db                  import IntegrityError
from django.core.paginator      import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth        import authenticate
from django.contrib             import auth
from PIL                        import Image

from .models import *
from .forms  import *

 
def register(request):
    false_message = ""
    user_form    = UserForm()
    profile_form = StudentProfileForm()
    
    if request.method == "POST":
		user_form    = UserForm(request.POST)
		profile_form = StudentProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user    = user_form.save()
			profile = profile_form.save(commit = False)

			profile.user = user
			profile.save()

    return render(request,'student/register.html',locals())
    
def profile(request, nick):
    context = []
    
    if request.method == "POST":
        pass
        
    user       = request.user
    authorized = request.user.is_authenticated()
    
    if authorized:
        profile = StudentProfile.objects.get(user=user)      
        context = {"profile":profile,}
    
    return render(request,'student/profile.html',context)
    
