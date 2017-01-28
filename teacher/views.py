# coding=utf-8

from django.http                    import HttpResponse, HttpResponseRedirect
from django.shortcuts               import render, get_object_or_404
from django.contrib                 import auth
from django.contrib.auth.decorators import login_required
from django.core.mail               import send_mass_mail
from django.db                      import IntegrityError

from teacher.models import *
from teacher.forms  import *

from main.views import sign_in, redirect_to_profile


### request handlers

def register(request):
    user_form    = UserForm()
    profile_form = TeacherProfileForm()

    if request.method == "POST":
		user_form    = UserForm(request.POST)
		profile_form = TeacherProfileForm(request.POST, request.FILES)

		if user_form.is_valid() and profile_form.is_valid():
			user    = user_form.save()
			profile = profile_form.save(commit = False)

			profile.user = user
			profile.save()

			username = user_form['username'].value()
			password = user_form['password'].value()

			user = sign_in(request, username, password)
			if user:
				return redirect_to_profile(user)

    return render(request, 'teacher/register.html', locals())
