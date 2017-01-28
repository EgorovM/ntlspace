# coding=utf-8

from django import forms

from main.forms                 import *
from student.models             import *
from django.contrib.auth.models import User

class StudentProfileForm(BootstrapModelForm):
    class Meta:
        model  = StudentProfile
        fields = ["name","birthdate","address","sex","grade","letter","avatar"]
    
