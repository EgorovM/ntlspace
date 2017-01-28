# coding=utf-8

from django import forms

from main.forms     import *
from teacher.models import *


class TeacherProfileForm(BootstrapModelForm):
    class Meta:
        model  = TeacherProfile
        fields = ['name', 'sex', 'birthdate', 'avatar', 'position', 'qualification', 'subject', 'education', 'educational_institution', 'work_experience', 'teaching_experience']
