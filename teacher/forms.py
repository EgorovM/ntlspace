# coding=utf-8

from django import forms

from main.forms     import *
from teacher.models import *


class TeacherProfileForm(BootstrapModelForm):
    class Meta:
        model  = TeacherProfile
        fields = ['name', 'sex', 'birthdate', 'avatar', 'position', 'qualification', 'subject', 'education', 'educational_institution', 'work_experience', 'teaching_experience']

        labels = {
            "name"                   : "Полное имя",
            "sex"                    : "Пол",
            "birthdate"              : "Дата рождения",
            "avatar"                 : "Аватар",
            "position"               : "Должность",
            "qualification"          : "Квалификация",
            "subject"                : "Предмет",
            "education"              : "Образование",
            "educational_institution": "Образовательное учреждение",
            "work_experience"        : "Общий стаж",
            "teaching_experience"    : "Педагогический стаж",
        }
