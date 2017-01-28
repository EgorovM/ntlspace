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

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 6:
            raise forms.ValidationError("Пароль слишком короткий, длина должна быть не менее 6 символов")

        return password

    def save(self, commit = True):
        instance = super(UserForm, self).save(commit = False)

        instance.set_password(self.cleaned_data['password'])

        if commit:
            instance.save()

        return instance
