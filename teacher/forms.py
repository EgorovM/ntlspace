# coding=utf-8

from django import forms

from teacher.models import *


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class TeacherProfileForm(BootstrapModelForm):
    class Meta:
        model  = TeacherProfile
        fields = ['name', 'sex', 'birthdate', 'avatar', 'position', 'qualification', 'subject', 'education', 'educational_institution', 'work_experience', 'teaching_experience']
