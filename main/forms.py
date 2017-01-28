# coding=utf-8

from django import forms
from django.contrib.auth.models import User


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class UserForm(BootstrapModelForm):
    class Meta:
        model  = User
        fields = ['username', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }
